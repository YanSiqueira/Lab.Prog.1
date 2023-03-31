import PySimpleGUI as sg
import functions

def Screen_login():
    #Componentes da janela
    layout_column = [[sg.Text("Login", size=(4,2), font=("", 25))],
            [sg.Text("Login:", size=(5,1), font=("", 15)), sg.Input(key='-login-', font=("", 15))],
            [sg.Text("Senha:", size=(5,1), font=("", 15)),sg.Input(key='-senha-', password_char='*', font=("", 15))],
            [sg.Text(key='-OUTPUT-', size =(40, 1), font=("", 15))],
            [sg.Button('Entrar', button_color=('white', 'green'), font=("", 15)), sg.Text("Fechar", enable_events=True, text_color=('dark red'), font=("", 10))]]
            
    layout = [[sg.Column(layout_column, element_justification='center')]]

    #cria a janela
    window = sg.Window('Locadora de Carros', layout)

    #loop da janela usando eventos
    while True:
        event, values = window.read()
        #fecha a janela
        if event == sg.WINDOW_CLOSED or event == 'Fechar':
            break
        #verifica login
        elif functions.check_password(values['-login-'], values['-senha-']) == True:
            Screen_menu()
            break
        else:
            window['-OUTPUT-'].update(' Login ou senha incorreto(s).')

    #encerra da janela
    window.close()

def Screen_menu():
    #Componentes da janela
    layout_column = [[sg.Text("Menu", font=("", 35), justification='center')],
            [sg.Text('Aluguel de Veiculo', enable_events=True, text_color=('white'), font=("", 20), justification='center')],
            [sg.Text('Clientes', enable_events=True, text_color=('white'), font=("", 20), justification='center')],
            [sg.Text('Funcionários', enable_events=True, text_color=('white'), font=("", 20), justification='center')],
            [sg.Text('Encerrar Sessão', enable_events=True, text_color=('dark red'), font=("", 15), justification='center')],
            [sg.Text("", size=(100,0))]]
            
    layout = [[sg.Column(layout_column, element_justification='center')]]

    #cria a janela
    window = sg.Window('Locadora de Carros', layout)

    #loop da janela usando eventos
    while True:
        event, values = window.read()
        if event == 'Aluguel de Veiculo':
            print("chama tela de aluguel de veiculo(a implementar)")
        elif event == 'Clientes':
             print("chama tela de cliente(a implementar)")
        elif event == 'Funcionários':
             print("chama tela de Funcionários(a implementar)")
        #fecha a janela
        elif event == sg.WINDOW_CLOSED or event == 'Encerrar Sessão':
            break

    #encerra da janela
    window.close()