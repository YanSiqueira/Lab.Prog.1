import PySimpleGUI as sg
import functions
import io
import os
import PySimpleGUI as sg
from PIL import Image
import pandas as pd
import base64

df_veicle_file = pd.read_excel('Files\\veicles.xlsx', index_col=0)

def Screen_login():
    #Componentes da janela
    layout_column = [[sg.Text("Login", font=("", 25))],
            [sg.Text("", font=("", 25))],
            [sg.Text("Login: ", font=("", 15)), sg.Input(key='-login-', font=("", 15))],
            [sg.Text("Senha:", font=("", 15)),sg.Input(key='-senha-', password_char='*', font=("", 15))],
            [sg.Text(key='-output-', size =(40, 1), font=("", 15), text_color=('dark red'))],
            [sg.Button('Entrar', button_color=('white', 'green'), font=("", 15))], [sg.Text("Criar nova conta", enable_events=True, text_color=('dark blue'), font=("", 10), justification='rigth', expand_x= True)]]
            
    layout = [[sg.Column(layout_column, element_justification='center', expand_x=True)]]

    #cria a janela
    window = sg.Window('Locadora de Carros', layout, finalize=True)

    #loop da janela usando eventos
    while True:
        event, values = window.read()
        #fecha a janela
        if event == sg.WINDOW_CLOSED:
            #encerra da janela
            break
        elif event == 'Criar nova conta':
            print('A implementar')
        #verifica login
        elif functions.check_password(values['-login-'], values['-senha-']) == True:
            window.close()
            #chama proxima tela
            Screen_menu()
        else:
            window['-output-'].update(' Login ou senha incorreto(s).')
    window.close()

def Screen_menu():
    d1=60
    d2=20
    d3=85
    #Componentes da janela
    layout_column = [[sg.Text("")],
            [sg.Text("Menu", font=("", 35))],
            [sg.Text("", font=("", d1))],
            [sg.Text('Aluguel de Veiculo', enable_events=True, text_color=('white'), font=("", 20))],
            [sg.Text("", font=("", d2))],
            [sg.Text('Clientes', enable_events=True, text_color=('white'), font=("", 20))],
            [sg.Text("", font=("", d2))],
            [sg.Text('Funcionários', enable_events=True, text_color=('white'), font=("", 20))],
            [sg.Text("", font=("", d2))],
            [sg.Text('Veículos', enable_events=True, text_color=('white'), font=("", 20))],
            [sg.Text("", font=("", d3))],
            [sg.Text('Encerrar Sessão', enable_events=True, text_color=('dark red'), font=("", 15), justification='rigth', expand_x= True)]]
            
    layout = [[sg.Column(layout_column, element_justification='center', expand_x=True)]]

    #cria a janela
    window = sg.Window('Locadora de Carros', layout, size=(600,600))

    #loop da janela usando eventos
    while True:
        event, values = window.read()
        if event == 'Aluguel de Veiculo':
            window.close()
            Scream_aluguel_veiculos()
        elif event == 'Clientes':
             print("chama tela de cliente(a implementar)")
        elif event == 'Funcionários':
             print("chama tela de Funcionários(a implementar)")
        elif event == 'Veículos':
            window.close()
            Scream_veiculos()
        #fecha a janela
        elif event == sg.WINDOW_CLOSED or event == 'Encerrar Sessão':
            break
    window.close()

def Scream_aluguel_veiculos():
    d1=60
    d2=20
    layout_column = [[sg.Text('Voltar',enable_events=True, justification='left', expand_x= True)],
            [sg.Text("Aluguel de Veiculo", font=("", 35))],
            [sg.Text("", font=("", d1))],
            [sg.Text('Iniciar Aluguel', enable_events=True, text_color=('white'), font=("", 20))],
            [sg.Text("", font=("", d2))],
            [sg.Text('Concluir Aluguel', enable_events=True, text_color=('white'), font=("", 20))],
            [sg.Text("", font=("", d2))],
            [sg.Text('Consultar Aluguel', enable_events=True, text_color=('white'), font=("", 20))]]
            
    layout = [[sg.Column(layout_column, element_justification='center', expand_x=True)]]

    window = sg.Window('Locadora de Carros', layout, size=(600,600))

    while True:
        event, values = window.read()
        if event == 'Iniciar Aluguel':
            print("chama tela de Iniciar Aluguel(a implementar)")
        elif event == 'Catálogo de veículos':
            print("chama tela de Encerar Aluguel(a implementar)")
        elif event == 'Consultar Aluguel':
            print("chama tela de Consultar Aluguel(a implementar)")
        elif event == 'Voltar':
            window.close()
            Screen_menu()
        elif event == sg.WINDOW_CLOSED:
            break
    window.close()

def Scream_veiculos():
    d1=60
    d2=20
    layout_column = [[sg.Text('Voltar',enable_events=True, justification='left', expand_x= True)],
            [sg.Text("Veículos", font=("", 35))],
            [sg.Text("", font=("", d1))],
            [sg.Text('Cadastrar Veículo', enable_events=True, text_color=('white'), font=("", 20))],
            [sg.Text("", font=("", d2))],
            [sg.Text('Editar veículo', enable_events=True, text_color=('white'), font=("", 20))],
            [sg.Text("", font=("", d2))],
            [sg.Text('Catálogo de Veículos', enable_events=True, text_color=('white'), font=("", 20))]]
            
    layout = [[sg.Column(layout_column, element_justification='center', expand_x=True)]]

    window = sg.Window('Locadora de Carros', layout, size=(600,600))

    while True:
        event, values = window.read()
        if event == 'Cadastrar Veículo':
            window.close()
            Screen_cadastrar_veiculo()
        elif event == 'Editar veículo':
            print("chama tela de Editar veículo(a implementar)")
        elif event == 'Catálogo de Veículos':
            window.close()
            Screen_tabela_veiculo()
        elif event == 'Voltar':
            window.close()
            Screen_menu()
        elif event == sg.WINDOW_CLOSED:
            break
    window.close()

def Screen_cadastrar_veiculo():
    d1=60
    file_types = [("JPEG (*.jpg)", "*.jpg"),
              ("All files (*.*)", "*.*")]
    layout_column = [[sg.Text('Voltar',enable_events=True, justification='left', expand_x= True)],
            [sg.Text("Inserir Veículo", font=("", 35), justification='center', expand_x= True)],
            [sg.Text("", font=("", d1))],
            [sg.Text('Fabricante:', text_color=('white'), font=("", 15)), sg.Input(key='-fabricante-', font=("", 15), size =(26,1)),
            sg.Text('Cor:', text_color=('white'), font=("", 15)), sg.Input(key='-cor-', font=("", 15), size=(6,1))],
            [sg.Text('       Modelo:', text_color=('white'), font=("", 15)), sg.Input(key='-modelo-', font=("", 15), size =(26,1)),
            sg.Text('Ano:', text_color=('white'), font=("", 15)), sg.Combo(['2023','2022','2021','2020','2019','2018'], default_value="2023", s=(15,22), enable_events=True, readonly=True, font=("", 15), size=(8,1), key='-ano-')],
            [sg.Text('   Descrição:', text_color=('white'), font=("", 15)), sg.Multiline(key='-descricao-', s=(38,2), font=("", 15))],
            [sg.Text('Alimentação:', text_color=('white'), font=("", 15)),sg.Combo(['Gasolina','Etanol','Gás','Elétrico','Híbrido','Dísel'], default_value="Gasolina", s=(15,22), enable_events=True, readonly=True, font=("", 15), size=(8,1), key='-alimentacao-'),
            sg.Text('Acentos:', text_color=('white'), font=("", 15)),sg.Combo(['2','4','5','6','7','8'], default_value=4, s=(15,22), enable_events=True, readonly=True, font=("", 15), size=(2,1), key='-acentos-'),
            sg.Text('Portas:', text_color=('white'), font=("", 15)),sg.Combo(['2','3','4'], default_value=4, s=(15,22), enable_events=True, readonly=True, font=("", 15), size=(2,1), key='-portas-')],
            [sg.Text(key='-output-',text_color=('dark red'), size =(40, 1), font=("", 15))],
            [sg.Text('  Chassi:', text_color=('white'), font=("", 15)), sg.Input(key='-chassi-', font=("", 15), justification='left', expand_x= True)],
            [sg.Text("Imagem:", text_color=('white'), font=("", 15)), sg.Input(size=(30, 1), font=("", 15), key="-file-"), sg.FileBrowse(file_types=file_types), sg.Button("Carregar")],
            [sg.Image(key="-imagem-"), sg.Button('Salvar', button_color=('white', 'green'), font=("", 15))]]
    
    layout = [[sg.Column(layout_column, element_justification='center', expand_x=True)]]
    window = sg.Window('Locadora de Carros', layout, size=(600,600))

    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Salvar":
            if values['-fabricante-'] != '' and values['-modelo-'] != '' and values['-descricao-'] != '' and values['-ano-'] != '' and values['-cor-'] != '' and values['-acentos-'] != '' and values['-portas-'] != '' and values['-file-'] != '' and values['-alimentacao-'] != '' and values['-chassi-'] != '':
                filename = values["-file-"]
                if os.path.exists(filename):
                    image = Image.open(values["-file-"])
                    image.thumbnail((150,150))
                    bio = io.BytesIO()
                    image.save(bio, format="PNG")
                    encoded_string = base64.b64encode(bio.getvalue())
                    encoded_string = encoded_string.decode('utf-8')
                    functions.insert_veicle(values['-chassi-'], values['-fabricante-'], values['-modelo-'], values['-ano-'],values['-alimentacao-'], values['-cor-'], values['-acentos-'], values['-portas-'],values['-descricao-'], encoded_string)
            else:
                window['-output-'].update('Informações Faltando.')
        elif event == "Voltar":
            window.close()
            Scream_veiculos()
        elif event == "Carregar":
            filename = values["-file-"]
            if os.path.exists(filename):
                image = Image.open(filename)
                image.thumbnail((200,200))
                bio = io.BytesIO()
                image.save(bio, format="PNG")
                window["-imagem-"].update(data=bio.getvalue())
    window.close()

def Screen_tabela_veiculo(index_list=range(0,len(df_veicle_file)), search=''):
    if search != '':
        tb = functions.table(functions.buscar_veiculo(search))
    else:
        tb = functions.table(index_list)
    layout=[[sg.Text('Voltar',enable_events=True, justification='left', expand_x= True)],
            [tb]]
    window = sg.Window("Locadora de Carros", layout,size=(1500,600), resizable=True, modal=True)
    while True:
        event, values = window.read()
        print("event:", event, "values:", values)
        if event == sg.WIN_CLOSED:
            break
        elif event == "Voltar":
            window.close()
            Scream_veiculos()
        elif '+CLICKED+' in event:
            sg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))    
    window.close()

def Scream_Pesquisar_veiculo():
    d1=60
    layout_column = [[sg.Text('Voltar',enable_events=True, justification='left', expand_x= True)],
            [sg.Text("Pesquisar Veículo", font=("", 35))],
            [sg.Text("", font=("", d1))],
            [sg.Text("Buscar:", font=("", 15)), sg.Input(size=(30, 1), font=("", 15), key="-search-", do_not_clear=False), sg.Button("Buscar"), sg.Button("Mostar tudo")]]
            
    layout = [[sg.Column(layout_column, element_justification='center', expand_x=True)]]
    window = sg.Window('Locadora de Carros', layout, resizable=True, size=(600,600))

    while True:
        event, values = window.read()
        if event == "Buscar" and values['-search-'] != '':
            sg.popup(Screen_tabela_veiculo(functions.table(functions.buscar_veiculo(values['-search-'])),values['-search-']))
        elif event == "Mostar tudo":
            sg.popup(Screen_tabela_veiculo())
        elif event == 'Voltar':
            window.close()
            Screen_menu()
        elif event == sg.WIN_CLOSED:
            break
    window.close()

def Scream_Pesquisar_veiculo():
    d1=60
    layout_column = [[sg.Text('Voltar',enable_events=True, justification='left', expand_x= True)],
            [sg.Text("Pesquisar Veículo", font=("", 35))],
            [sg.Text("", font=("", d1))],
            [sg.Text("Buscar:", font=("", 15)), sg.Input(size=(30, 1), font=("", 15), key="-search-", do_not_clear=False), sg.Button("Buscar"), sg.Button("Mostar tudo")]]
            
    layout = [[sg.Column(layout_column, element_justification='center', expand_x=True)]]
    window = sg.Window('Locadora de Carros', layout, resizable=True, size=(600,600))

    while True:
        event, values = window.read()
        if event == "Buscar" and values['-search-'] != '':
            sg.popup(Screen_tabela_veiculo(functions.table(functions.buscar_veiculo(values['-search-'])),values['-search-']))
        elif event == "Mostar tudo":
            sg.popup(Screen_tabela_veiculo())
        elif event == 'Voltar':
            window.close()
            Screen_menu()
        elif event == sg.WIN_CLOSED:
            break
    window.close()