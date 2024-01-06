"""

We are starting with GUI on Day 16

"""
import PySimpleGUI as gui
import functions as fn

label = gui.Text("Type in a To-Do")
input_box = gui.InputText(tooltip="Enter todo", key="todo")
add_button = gui.Button("Add")
list_box = gui.Listbox(values=fn.read_file(), key="l_todo", enable_events=True, size=(45, 10))
edit_button = gui.Button("Edit")
exit_button = gui.Button("Exit")


window = gui.Window("To-Do App", layout=[[label], [input_box, add_button], [list_box,edit_button]],
                    font=('Helvetica', 16))

while True:
    event, values = window.read()

    match event:
        case "Add":
            todos = fn.read_file()
            new_todo = values["todo"]+"\n"
            todos.append(new_todo)
            fn.write_file(todos)
            window['l_todo'].update(values=fn.read_file())
        case "Edit":
            todo_to_edit = values["l_todo"][0]
            new_todo = values["todo"]
            todos = fn.read_file()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            fn.write_file(todos)
            window['l_todo'].update(values=fn.read_file())
        case "l_todo":
            window['todo'].update(value=values['l_todo'][0])
        case gui.WIN_CLOSED:
            break


window.close()

