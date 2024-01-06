"""

We are starting with GUI on Day 16

"""
import PySimpleGUI as gui
import functions

label = gui.Text("Type in a to-do")
input_box = gui.InputText(tooltip="Enter todo")
add_button = gui.Button("Add")


window = gui.Window("To-Do App", layout=[[label], [input_box], [add_button]])
window.read()
window.close()
