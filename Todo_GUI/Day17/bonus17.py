import PySimpleGUI as gui
import zipper

label_file = gui.Text("Select the Source file: ")
label_destination = gui.Text("Select the Target path: ")
label_success = gui.Text(key="success")

input_box_src = gui.Input()
input_box_tgt = gui.Input()

choose_src = gui.FilesBrowse("Choose", key="src_files")
choose_tgt = gui.FolderBrowse("Choose", key="tgt_loc")

btn_compress = gui.Button("Compress")

window = gui.Window("Zipper", layout=[[label_file, input_box_src, choose_src],
                                      [label_destination, input_box_tgt, choose_tgt],
                                      [btn_compress, label_success]])

while True:
    event, values = window.read()
    match event:
        case gui.WIN_CLOSED:
            break

    folder = values["tgt_loc"]
    files = values["src_files"].split(";")
    zipper.make_archive(files, folder)
    window["success"].update(value="Compression Completed.")


window.close()
