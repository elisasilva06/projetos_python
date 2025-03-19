import PySimpleGUI as sg

def janela_inicial():
    sg.theme('purple')
    linha = [
        [sg.Input(''),sg.Checkbox('')]
    ]
    layout = [
        [sg.Frame('Minhas Tarefas',layout=linha,key='container')],
        [sg.Button('Nova Tarefa'),sg.Button('Resetar')]
    ]

    return sg.Window('Todo List',layout=layout,finalize=True)

janela = janela_inicial()

while True:
    event, value = janela.read()
    if event == sg.WIN_CLOSED:
        break
    if event == 'Nova Tarefa':
        janela.extend_layout(janela['container'],[[sg.Input(''),sg.Checkbox('')]])

