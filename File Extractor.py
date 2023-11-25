import PySimpleGUI as sg
from zip_extractor import *

sg.theme("Black")

label1 = sg.Text("Select Zip Dir: ")
input1 = sg.Input()
bun_1 = sg.FileBrowse("Choose", key="archieve")

label2 = sg.Text("Select Dist Dir: ")
input2 = sg.Input()
bun_2 = sg.FolderBrowse("Choose", key="folder")

extract_btn = sg.Button("Extract")
extract_lbl = sg.Text("", key="status", text_color="green")

window = sg.Window("File Extractor", layout=[[label1, input1, bun_1], [
                   label2, input2, bun_2], [extract_btn, extract_lbl]])

while True:
    event, values = window.read()
    # print(event, values)
    match event:
        case "Extract":
            dist = values['folder']
            zipion = values['archieve']
            extract_archive(zipion, dist)
            window['status'].update(value="Extraction Completed!")
        case sg.WIN_CLOSED:
            break
window.close()
