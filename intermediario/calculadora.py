import PySimpleGUI as sg
import re, sys 

sg.theme('LightBlue')


layout = [
    [sg.Multiline("", size=(25, 5), key="-display-", justification="r", font="digit 20 ", no_scrollbar=True)],
    [sg.Button("C", size=(3,3)), sg.Button("(", size=(3,3)), sg.Button(")", size=(3,3)), sg.Button("/", size=(3,3))],
    [sg.Button("7", size=(3,3)), sg.Button("8", size=(3,3)), sg.Button("9", size=(3,3)), sg.Button("*", size=(3,3))],
    [sg.Button("4", size=(3,3)), sg.Button("5", size=(3,3)), sg.Button("6", size=(3,3)), sg.Button("-", size=(3,3))],
    [sg.Button("1", size=(3,3)), sg.Button("2", size=(3,3)), sg.Button("3", size=(3,3)), sg.Button("+", size=(3,3))],
    [sg.Button("0", size=(3,3)), sg.Button(".", size=(3,3)), sg.Button("%", size=(3,3)), sg.Button("=", size=(3,3))]   
]

window = sg.Window("CALCULADORA", layout=layout, element_justification="center")

window.read()