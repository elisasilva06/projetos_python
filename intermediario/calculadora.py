import PySimpleGUI as sg
import re, sys 

sg.theme('LightBlue')

def calcular(conta):
    try:
        conta = conta.replace('%', '/100')
        return str(eval(conta))
    except Exception as e:
        return "ERRO..." 
          



layout = [
    [sg.Multiline("", size=(20, 3), key="-display-", justification="r", font="Helvetica 20", no_scrollbar=True)],
    [sg.Button("%", size=(2,2), button_color=('DarkBlue')), sg.Button("(", size=(2,2), button_color=('DarkBlue')), sg.Button(")", size=(2,2), button_color=('DarkBlue')), sg.Button("/", size=(2,2), button_color=('DarkBlue'))],
    [sg.Button("7", size=(2,2)), sg.Button("8", size=(2,2)), sg.Button("9", size=(2,2)), sg.Button("*", size=(2,2), button_color=('DarkBlue'))],
    [sg.Button("4", size=(2,2)), sg.Button("5", size=(2,2)), sg.Button("6", size=(2,2)), sg.Button("-", size=(2,2), button_color=('DarkBlue'))],
    [sg.Button("1", size=(2,2)), sg.Button("2", size=(2,2)), sg.Button("3", size=(2,2)), sg.Button("+", size=(2,2), button_color=('DarkBlue'))],
    [sg.Button("0", size=(2,2)), sg.Button(".", size=(2,2)), sg.Button("=", size=(2,2)), sg.Button("C", size=(2,2), button_color=('DarkBlue'))]   
]

window = sg.Window("ANA ELISA ", layout=layout, element_justification="center")

conta = ""

while True:
    
    event,values = window.read()

    if event == sg.WIN_CLOSED:
        break
    if event in("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "/", "*", "-", "+", "(", ")", ):
        conta += str(event)
        window["-display-"].update(conta) 

    elif event == 'C':
        conta = ""
        window["-display-"].update(conta)

    elif event == '=':
        if conta == "" or conta[-1] in "+-*/":
            resposta = "ERRO"
        else: 
            resposta = calcular(conta)
        window["-display-"].update(resposta)
        conta = resposta 

    
             

    
        

         



    

    

window.close()