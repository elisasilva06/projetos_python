import PySimpleGUI as sg
import re, sys 

sg.theme('LightBlue')




layout = [
    [sg.Multiline("", size=(20, 3), key="-display-", justification="r", font="Helvetica 20", no_scrollbar=True)],
    [sg.Button("C", size=(2,2), button_color=('DarkBlue')), sg.Button("(", size=(2,2), button_color=('DarkBlue')), sg.Button(")", size=(2,2), button_color=('DarkBlue')), sg.Button("/", size=(2,2), button_color=('DarkBlue'))],
    [sg.Button("7", size=(2,2)), sg.Button("8", size=(2,2)), sg.Button("9", size=(2,2)), sg.Button("*", size=(2,2), button_color=('DarkBlue'))],
    [sg.Button("4", size=(2,2)), sg.Button("5", size=(2,2)), sg.Button("6", size=(2,2)), sg.Button("-", size=(2,2), button_color=('DarkBlue'))],
    [sg.Button("1", size=(2,2)), sg.Button("2", size=(2,2)), sg.Button("3", size=(2,2)), sg.Button("+", size=(2,2), button_color=('DarkBlue'))],
    [sg.Button("0", size=(2,2)), sg.Button(".", size=(2,2)), sg.Button("=", size=(2,2)), sg.Button("%", size=(2,2), button_color=('DarkBlue'))]   
]

window = sg.Window("ANA ELISA ", layout=layout, element_justification="center")

window.read()