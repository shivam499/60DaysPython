import sqlite3
import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLineEdit, QPushButton, QMainWindow, QTableWidget, \
    QTableWidgetItem, QDialog, QVBoxLayout, QComboBox, QToolBar, QStatusBar, QLabel, QMessageBox, QGridLayout
from PyQt6.QtGui import QAction, QIcon


class DatabaseConnection:
    def __init__(self, database="database.db"):
        self.database = database

    def connect(self):
        connection_sqlite = sqlite3.connect(self.database)
        return connection_sqlite


class StudentManagement(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800,600)

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        add_student_action = QAction(QIcon("icons/add.png"), "Add Student",self)
        add_student_action.triggered.connect(self.insert)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About",self)
        help_menu_item.addAction(about_action)
        about_action.triggered.connect(self.about_page)

        search_action = QAction(QIcon("icons/search.png"), "Search",self)
        search_action.triggered.connect(self.search)
        edit_menu_item.addAction(search_action)

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id","Name","Course","Mobile"))
        self.table.verticalHeader().setVisible(False)

        self.setCentralWidget(self.table)

        #Create Toolbar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        #Create Status Bar
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)

        self.table.cellClicked.connect(self.cell_clicked)

    def about_page(self):
        dialog = AboutMessageDialog()
        dialog.exec()

    def cell_clicked(self):
        edit_button = QPushButton("Edit Student")
        edit_button.clicked.connect(self.edit_Student)

        delete_button = QPushButton("Delete Student")
        delete_button.clicked.connect(self.delete_Student)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)

        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def load_data(self):
        connection_load = DatabaseConnection().connect()
        result = connection_load.execute("SELECT * FROM students")
        self.table.setRowCount(0)
        for row_num,row_data in enumerate(result):
            self.table.insertRow(row_num)
            for col_num, data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QTableWidgetItem(str(data)))
        connection_load.close()
    
    def insert(self):
        dialog = InsertDialog()
        dialog.exec()

    def search(self):
        dialog = SearchDialog()
        dialog.exec()

    def edit_Student(self):
        dialog = EditDialog()
        dialog.exec()

    def delete_Student(self):
        dialog = DeleteDialog()
        dialog.exec()

class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout(self)

        index = window.table.currentRow()
        student_name = window.table.item(index, 1).text()
        course = window.table.item(index,2).text()
        phone = window.table.item(index, 3).text()

        self.student_id = window.table.item(index,0).text()

        # Name input
        self.student_input = QLineEdit(student_name)
        layout.addWidget(self.student_input)

        # Course selection
        self.course_input = QComboBox()
        courses = ["Biology","Maths","Astronomy","Physics"]
        self.course_input.addItems(courses)
        self.course_input.setCurrentText(course)
        layout.addWidget(self.course_input)

        # Mobile input
        self.phone_input = QLineEdit(phone)
        layout.addWidget(self.phone_input)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.update_student)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def update_student(self):
        name = self.student_input.text()
        course = self.course_input.itemText(self.course_input.currentIndex())
        phone = self.phone_input.text()
        connection_update = DatabaseConnection().connect()
        cursor = connection_update.cursor()
        cursor.execute("UPDATE students SET name = ?, course = ?, mobile = ? WHERE id = ?",
                       (name, course, phone,self.student_id))

        connection_update.commit()
        cursor.close()
        connection_update.close()

        window.load_data()

class AboutMessageDialog(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """
        This app is created during the courses "The Python Mega Course."
        Feel free to connect with us
        """
        self.setText(content)

class DeleteDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student Data")

        layout = QGridLayout(self)

        label_delete = QLabel("Are you sure to delete this Student records?")
        layout.addWidget(label_delete,0,0,1,2)

        no_button = QPushButton("No")
        layout.addWidget(no_button,1, 0)

        self.yes_button = QPushButton("Yes")
        self.yes_button.clicked.connect(self.delete_student)
        layout.addWidget(self.yes_button,1,1)

        self.setLayout(layout)

    def delete_student(self):
        index = window.table.currentRow()
        stu_id = window.table.item(index, 0).text()

        connection_delete = DatabaseConnection().connect()
        cursor = connection_delete.cursor()
        cursor.execute("DELETE from students WHERE id = ? ", (stu_id,))

        connection_delete.commit()
        cursor.close()
        connection_delete.close()

        window.load_data()

        self.close()

        confirmation_widget = QMessageBox()
        confirmation_widget.setWindowTitle("Success")
        confirmation_widget.setText("The record was deleted successfully!")
        confirmation_widget.exec()


class SearchDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Search Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout(self)

        # Name input
        self.name_search = QLineEdit()
        self.name_search.setPlaceholderText("Name")
        layout.addWidget(self.name_search)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.search_student)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def search_student(self):
        name = self.name_search.text()
        connection_insert = DatabaseConnection().connect()
        cursor = connection_insert.cursor()
        cursor.execute("SELECT * from students WHERE name = ? ", (name,))
        items = window.table.findItems(name,Qt.MatchFlag.MatchFixedString)

        for item in items:
            window.table.item(item.row(),1).setSelected(True)

        cursor.close()
        connection_insert.close()


class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student")
        self.setFixedWidth(300)
        self.setFixedHeight(300)

        layout = QVBoxLayout(self)

        # Name input
        self.name_input = QLineEdit()
        self.name_input.setPlaceholderText("Name")
        layout.addWidget(self.name_input)

        # Course selection
        self.course_input = QComboBox()
        courses = ["Biology","Maths","Astronomy","Physics"]
        self.course_input.addItems(courses)
        layout.addWidget(self.course_input)

        # Mobile input
        self.phone_input = QLineEdit(self)
        self.phone_input.setPlaceholderText("Mobile")
        layout.addWidget(self.phone_input)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit)
        layout.addWidget(self.submit_button)

        self.setLayout(layout)

    def submit(self):
        name = self.name_input.text()
        course = self.course_input.itemText(self.course_input.currentIndex())
        phone = self.phone_input.text()
        connection_insert = DatabaseConnection().connect()
        cursor = connection_insert.cursor()
        cursor.execute("INSERT INTO students (name, course, mobile) VALUES (?, ?, ?)",
                       (name, course, phone))

        connection_insert.commit()
        cursor.close()
        connection_insert.close()

        window.load_data()


app = QApplication(sys.argv)
window = StudentManagement()
window.show()
window.load_data()
sys.exit(app.exec())
