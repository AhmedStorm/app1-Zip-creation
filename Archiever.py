import PySimpleGUI as sg
from zip_creator import *
file_txt = sg.Text("Choose Files to Compress")
files_inp = sg.InputText()
files_btn = sg.FilesBrowse("Browse Files")
fld_txt = sg.Text("Choose Output Directory")
fld_inp = sg.InputText()
fld_btn = sg.FolderBrowse("Browse Folder")

compress_btn = sg.Button("Compress")
output_txt = sg.Text(key="output", text_color="green")

window = sg.Window("Files Compressor", layout=[
                   [file_txt, files_inp, files_btn],
                   [fld_txt, fld_inp, fld_btn],
                   [compress_btn, output_txt]])
while True:
    event, values = window.read()
    # print(event, values)
    file_paths = values["Browse Files"].split(" ;")
    dir_path = values["Browse Folder"]
    # print(file_paths, dir_path)
    make_archieve(file_paths, dir_path)
    window["output"].update(value="Compression Completed!")


window.close()
