import PySimpleGUI as sg
import functions
import io
import os
import PySimpleGUI as sg
from PIL import Image
import pandas as pd
import base64
import datetime

df_veicle_file = pd.read_excel('Files\\veicles.xlsx', index_col=0)
df_aluguel_file = pd.read_excel('Files\\aluguel.xlsx', index_col=0)

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
            window.close()
            Scream_iniciar_aluguel_veiculo()
        elif event == 'Concluir Aluguel':
            window.close()
            Scream_concuir_aluguel_veiculo()
        elif event == 'Consultar Aluguel':
            Screen_tabela_aluguel()
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
    row =''
    if search != '':
        tb = functions.table(functions.buscar_veiculo(search))
    else:
        tb = functions.table(index_list)
    layout=[[sg.Text('Voltar',enable_events=True, justification='left', expand_x= True)],
            [tb]]
    window = sg.Window("Locadora de Carros", layout,size=(1500,600), resizable=True, modal=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Voltar":
            break
        elif '+CLICKED+' in event:
            if search != '':
                row = functions.table(functions.buscar_veiculo(search),True)[event[2][0]]
            else:
                row = functions.table(index_list,True)[event[2][0]]
    
    window.close()      
    return row    

def Screen_tabela_aluguel(index_list=range(0,len(df_aluguel_file)), search=''):
    row =''
    if search != '':
        tb = functions.table_aluguel(functions.buscar_aluguel(search))
    else:
        tb = functions.table_aluguel(index_list)
    layout=[[sg.Text('Voltar',enable_events=True, justification='left', expand_x= True)],
            [tb]]
    window = sg.Window("Locadora de Carros", layout,size=(1500,600), resizable=True, modal=True)
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Voltar":
            break
        elif '+CLICKED+' in event:
            if search != '':
                row = functions.table_aluguel(functions.buscar_aluguel(search),True)[event[2][0]]
            else:
                row = functions.table_aluguel(index_list,True)[event[2][0]]
    
    window.close()
    if row != '':
        return row    
    

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
            Screen_tabela_veiculo(functions.table(functions.buscar_veiculo(values['-search-'])),values['-search-'])
        elif event == "Mostar tudo":
            Screen_tabela_veiculo()
        elif event == 'Voltar':
            window.close()
            Screen_menu()
        elif event == sg.WIN_CLOSED:
            break
    window.close()

def Scream_iniciar_aluguel_veiculo():
    layout_column = [[sg.Text('Voltar',enable_events=True, justification='left', expand_x= True)],
            [sg.Text("Alugar Veículo", font=("", 35), justification='center', expand_x= True)],
            [sg.Text("", font=("", 35))],
            [sg.Text("~ Informações do cliente ~", text_color=('white'), font=("", 15), justification='center', expand_x= True)],
            [sg.Text('       CPF:', text_color=('white'), font=("", 15)), sg.Input(key='-cpf-', font=("", 15), size =(26,1), justification='left', expand_x= True)],
            [sg.Text('     Nome:', text_color=('white'), font=("", 15)), sg.Input(key='-nome-', font=("", 15), size =(26,1), justification='left', expand_x= True)],
            [sg.Text('  Contato:', text_color=('white'), font=("", 15)), sg.Input(key='-contato-', font=("", 15), size=(26,1), justification='left', expand_x= True)],
            [sg.Text('Endereço:', text_color=('white'), font=("", 15)), sg.Input(key='-endereco-', font=("", 15), size=(26,1), justification='left', expand_x= True),
            sg.Text('Número:', text_color=('white'), font=("", 15)), sg.Input(key='-numero-', font=("", 15), size=(6,1), justification='left', expand_x= True)],
            [sg.Text("~ Informações do Aluguel ~",text_color=('white'), font=("", 15), justification='center', expand_x= True)],
            [sg.Text('Diária:', text_color=('white'), font=("", 15)), sg.Input(key='-diaria-', font=("", 15), size =(7,1)),
            sg.Text('Atraso:', text_color=('white'), font=("", 15)), sg.Input(key='-atraso-', font=("", 15), size =(7,1)),
            sg.Text('Taxa:', text_color=('white'), font=("", 15)), sg.Input(key='-taxa-', font=("", 15), size =(7,1))],
            [sg.CalendarButton('Data Início:', target='-inicio-', pad=None, key='_CALENDAR_', format=('%d/%m/%Y')),
            sg.In(key='-inicio-', enable_events=True, size =(12,1), font=("", 15)),
            sg.CalendarButton('Data Fim:', target='-fim-', pad=None, key='_CALENDAR_', format=('%d/%m/%Y')),
            sg.In(key='-fim-', enable_events=True, size =(12,1), font=("", 15)), sg.Button("Calcular")],
            [sg.Text('Valor Parcial:', text_color=('white'), font=("", 15)), sg.Text(key='-valor-', size =(40, 1), font=("", 15), text_color=('dark green'))],
            [sg.Text("~ Veículo ~", text_color=('white'), font=("", 15), justification='center', expand_x= True)],
            [sg.Text("Veículo:", font=("", 15)), sg.Input(size=(29, 1), font=("", 15), key="-search-"), sg.Button("Buscar"), sg.Button("Mostar tudo")],
            [sg.Text(key='-veiculo-', size =(40, 1), font=("", 10), justification='center', expand_x= True)],
            [sg.Button("Concluir", font=("", 15), button_color=('dark green'))]]
            
    layout = [[sg.Column(layout_column, element_justification='center', expand_x=True)]]
    window = sg.Window('Locadora de Carros', layout, resizable=True, size=(600,600))

    while True:
        event, values = window.read()
        if event == "Buscar" and values['-search-'] != '':
            try:
                veiculo = Screen_tabela_veiculo(functions.table(functions.buscar_veiculo(values['-search-'])),values['-search-'])[0:6]
            except:
                veiculo = ''
            finally:
                window['-veiculo-'].update(veiculo)
        elif event == "Mostar tudo":
            try:
                veiculo = Screen_tabela_veiculo()[0:6]
            except:
                veiculo = ''
            finally:
                window['-veiculo-'].update(veiculo)
        elif event == 'Voltar':
            window.close()
            Scream_aluguel_veiculos()
        elif event == 'Calcular':
            if values['-inicio-'] != '' and values['-fim-'] != '' and values['-diaria-'] != '':
                valor = (functions.diferenca_data(values['-inicio-'], values['-fim-']) * float(values['-diaria-']))
                window['-valor-'].update(valor)
        elif event == 'Concluir':
            if values['-cpf-'] != '' and values['-nome-'] != '' and values['-endereco-'] != '' and values['-numero-'] != '' and values['-contato-'] != '' and values['-diaria-'] != '' and values['-atraso-'] != '' and values['-taxa-'] != '' and values['-inicio-'] != '' and values['-fim-'] != ''and veiculo != '':
                functions.inserir_aluguel(values['-cpf-'], values['-nome-'], values['-contato-'], values['-endereco-'], values['-numero-'], values['-inicio-'], values['-fim-'],values['-diaria-'], values['-atraso-'], values['-taxa-'], valor, veiculo[0])
                window['-valor-'].update('')
                sg.popup("Operação bem sucedida!")
                window.close()
                Scream_aluguel_veiculos()
        elif event == sg.WIN_CLOSED:
                break
    window.close()

def Scream_concuir_aluguel_veiculo():
    valor=''
    layout_column = [[sg.Text('Voltar',enable_events=True, justification='left', expand_x= True)],
            [sg.Text("Concluir Aluguel Veículo", font=("", 35), justification='center', expand_x= True)],
            [sg.Text("", font=("", 35))],
            [sg.Text("Aluguel:", font=("", 15)), sg.Input(size=(29, 1), font=("", 15), key="-search-", do_not_clear=False), sg.Button("Buscar"), sg.Button("Mostar tudo")],
            [sg.Text(key='-aluguel-', size =(40, 1), font=("", 10), justification='center', expand_x= True)],
            [sg.Button("Calcular"), sg.Text('Valor Final:', text_color=('white'), font=("", 15)), sg.Text(key='-valor-', size =(40, 1), font=("", 15), text_color=('dark green'))],
            [sg.Button("Concluir", font=("", 15), button_color=('dark green'))]]
            
    layout = [[sg.Column(layout_column, element_justification='center', expand_x=True)]]
    window = sg.Window('Locadora de Carros', layout, resizable=True, size=(600,600))

    while True:
        event, values = window.read()
        if event == "Buscar" and values['-search-'] != '':
            try:
                aluguel = Screen_tabela_aluguel(functions.table_aluguel(functions.buscar_aluguel(values['-search-'])),values['-search-'])[0:6]
            except:
                aluguel = ''
            finally:
                window['-aluguel-'].update(aluguel)
        elif event == "Mostar tudo":
            try:
                aluguel = Screen_tabela_aluguel()
            except:
                aluguel = ''
            finally:
                window['-aluguel-'].update(aluguel[5:10])
        elif event == 'Voltar':
            window.close()
            Scream_aluguel_veiculos()
        elif event == 'Calcular':
            if  functions.diferenca_data(aluguel[5], datetime.date.today()) == 0:
                valor = aluguel[10]
                window['-valor-'].update(valor)
            elif functions.diferenca_data(aluguel[5], datetime.date.today()) < 0:
                valor = (functions.diferenca_data(aluguel[5], datetime.date.today()) * float(aluguel[6]))
                window['-valor-'].update(valor)
            elif functions.diferenca_data(aluguel[5], datetime.date.today()) > 0:
                valor = ((functions.diferenca_data(aluguel[6], datetime.date.today()) * (float(aluguel[8]))) + float(aluguel[7] + float(aluguel[9])))
                window['-valor-'].update(valor)
        elif event == 'Concluir':
            if  valor != '':
                functions.concluir_aluguel(aluguel[11], valor)
                sg.popup("Operação bem sucedida!")
                window['-valor-'].update('')
        elif event == sg.WIN_CLOSED:
                break
    window.close()
