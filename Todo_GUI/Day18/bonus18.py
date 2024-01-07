import PySimpleGUI as gui
import zipper

gui.theme("Black")

label_file = gui.Text("Select archive file: ")
label_destination = gui.Text("Select the Target path: ")
label_success = gui.Text(key="success")

input_box_src = gui.Input()
input_box_tgt = gui.Input()

choose_src = gui.FilesBrowse("Choose", key="archive")
choose_tgt = gui.FolderBrowse("Choose", key="target")

btn_extract = gui.Button("Extract")

window = gui.Window("Zipper", layout=[[label_file, input_box_src, choose_src],
                                      [label_destination, input_box_tgt, choose_tgt],
                                      [btn_extract, label_success]])

while True:
    event, values = window.read()
    match event:
        case "Extract":
            archive_path = values["archive"]
            tgt_dir = values["target"]
            zipper.extract_archive(archive_path, tgt_dir)
            window["success"].update(value="Extraction completed.")
        case gui.WIN_CLOSED:
            break


window.close()
