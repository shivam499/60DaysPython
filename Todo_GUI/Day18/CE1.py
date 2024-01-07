import PySimpleGUI as gui


def convert(feet, inch):
    meter = feet * 0.3048 + inch * 0.0254
    return meter


label_feet = gui.Text("Enter feet:")
label_inch = gui.Text("Enter inches:")

feet_input = gui.Input("0", key="feet")
inch_input = gui.Input("0", key="inch")

btn_convert = gui.Button("Convert", key="convert")
btn_exit = gui.Button("Exit", key="exit")
lbl_result = gui.Text(key="result")

col1 = gui.Column([[label_feet], [label_inch]])
col2 = gui.Column([[feet_input], [inch_input]])

window = gui.Window("Convertor", layout=[[col1, col2],
                                         [btn_convert, btn_exit, lbl_result]])

while True:
    event, values = window.read()

    match event:
        case "convert":
            meters = f"{round(convert(float(values["feet"]), float(values["inch"])), 3)} m"
            window["result"].update(value=meters)
        case "exit":
            break
        case gui.WIN_CLOSED:
            break

window.close()
