import PySimpleGUI as sg

def janela_inicial():
    sg.theme('Purple')
    
    # Linha base para tarefas
    linha = [[sg.Input(''), sg.Checkbox('', key=f'chk_0', enable_events=True)]]

    layout = [
        [sg.Frame('Minhas Tarefas', layout=linha, key='container')],
        [sg.ProgressBar(100, orientation='h', size=(20, 20), key='progress_bar')],
        [sg.Button('Nova Tarefa'), sg.Button('Resetar')]
    ]

    return sg.Window('Todo List', layout=layout, finalize=True), 1  # Retorna a janela e o contador inicial de tarefas

janela, total_tarefas = janela_inicial()
tarefas_concluidas = 0  # Contador de tarefas concluídas

while True:
    event, value = janela.read()

    if event == sg.WIN_CLOSED:
        break

    elif event == 'Nova Tarefa':
        total_tarefas += 1  # Atualiza o total de tarefas
        nova_linha = [sg.Input(''), sg.Checkbox('', key=f'chk_{total_tarefas}', enable_events=True)]
        janela.extend_layout(janela['container'], [nova_linha])

    elif event == 'Resetar':
        janela.close()
        janela, total_tarefas = janela_inicial()  # Reinicializa corretamente
        tarefas_concluidas = 0

    elif event.startswith('chk_'):
        if value[event]:  # Se a checkbox for marcada
            tarefas_concluidas += 1
        else:  # Se for desmarcada
            tarefas_concluidas -= 1

        # Atualiza a barra de progresso
        progresso = (tarefas_concluidas / total_tarefas) * 100
        janela['progress_bar'].update(progresso)

janela.close()
