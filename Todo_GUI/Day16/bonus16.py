import PySimpleGUI as gui

label_file = gui.Text("Select the Source file: ")
label_destination = gui.Text("Select the Target path: ")

input_box_src = gui.Input()
input_box_tgt = gui.Input()

choose_src = gui.FilesBrowse("Choose")
choose_tgt = gui.FolderBrowse("Choose")

btn_compress = gui.Button("Compress")

window = gui.Window("Zipper", layout=[[label_file, input_box_src, choose_src],
                                      [label_destination, input_box_tgt, choose_tgt],
                                      [btn_compress]])

window.read()
window.close()