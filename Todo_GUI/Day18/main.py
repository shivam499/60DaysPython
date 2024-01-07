"""

We are starting with GUI on Day 16

"""
import time

import PySimpleGUI as gui
import functions as fn
import os

# pyinstaller --onefile --windowed --clean main.py

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

gui.theme("Black")

clock = gui.Text(key="clock")
label = gui.Text("Type in a To-Do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")

add_button = gui.Button("Add", key="Add", size=10, mouseover_colors="LightBlue2", tooltip="Add todo")
list_box = gui.Listbox(values=fn.read_file(), key="l_todo", enable_events=True, size=(45, 10))
edit_button = gui.Button("Edit")
btn_complete = gui.Button("Complete", key="complete")
exit_button = gui.Button("Exit")


window = gui.Window("To-Do App", layout=[[clock], [label], [input_box, add_button],
                                         [list_box, edit_button, btn_complete],
                                         [exit_button]],
                    font=('Helvetica', 16))

while True:
    event, values = window.read(timeout=10)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case "Add":
            todos = fn.read_file()
            if len(str(values["todo"]).strip(' ')) == 0:
                gui.popup("Please enter a To-do")
            else:
                new_todo = values["todo"] + "\n"
                todos.append(new_todo)
                fn.write_file(todos)
                window['l_todo'].update(values=fn.read_file())
        case "Edit":
            try:
                todo_to_edit = values["l_todo"][0]
                new_todo = values["todo"] + "\n"
                todos = fn.read_file()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                fn.write_file(todos)
                window['l_todo'].update(values=fn.read_file())
            except IndexError:
                gui.popup("Please select the todo.", font=("Open Sans", 16))
        case "l_todo":
            window['todo'].update(value=values['l_todo'][0])
        case "complete":
            try:
                todo_to_complete = values["l_todo"][0]
                todos = fn.read_file()
                todos.remove(todo_to_complete)
                fn.write_file(todos)
                window["l_todo"].update(values=fn.read_file())
                window["todo"].update(value="")
            except IndexError:
                gui.popup("Please select the todo.", font=("Open Sans", 16))
        case "Exit":
            break
        case gui.WIN_CLOSED:
            break


window.close()
