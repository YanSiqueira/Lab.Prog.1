import pandas as pd
import numpy as np
import PySimpleGUI as sg

'''
import os
def check_files(files_list):
    for file in files_list:
        if not os.path.exists(f'Files\\{file}'):
            try:
                open(f'Files\\{file}', 'w')
                
            except IOError:
                os.makedirs('Files')
                open(f'Files\\{file}', 'w')

#check_files(['Veiculos', 'Clientes', 'Funcionarios', 'Historico de Locações'])

def load_loging_file():
    try:
        df = pd.read_excel('files\\loging.xlsx')
    except IOError:
        print()
'''
#cria(se não existir) arquivo e insere login para se poder testar o login
def create_login():
    try:
        df_login_file = pd.read_excel('Files\\login.xlsx', index_col=0)
        #pega  linhas vazias, se houver
        na = df_login_file.index[df_login_file['Count_id'].isna() == True].tolist()
        try:
            #tenta add na primeira linha vazia
            df_login_file.loc[na[0],["Count_id", "Login", "Senha"]] = [1,'yan','123']
        except IndexError:
            #add no final da planilha
            df_login_file.loc[len(df_login_file),["Count_id", "Login", "Senha"]] = [1,'yan','123']
        finally:    
            df_login_file.to_excel('Files\\login.xlsx')
    except FileNotFoundError:
        #cria o arquivo se ele não exixtir
        df_file_login =  pd.DataFrame(columns=["Count_id", "Login", "Senha"], index=[0])
        df_file_login.to_excel('Files\\login.xlsx')

#verifica se um login existe na planilha
def check_if_login_exists(login):
    df_login_file = pd.read_excel('Files\\login.xlsx', index_col=0)
    if df_login_file.index[df_login_file['Login'] == str(login)].tolist() != []:
        return True
    else:
        return False
    
#verifica se a senha digitada bate com a respectiva senha do login
def check_password(login, password):
    if check_if_login_exists(login) == True:
        df_login_file = pd.read_excel('Files\\login.xlsx', index_col=0)
        index = df_login_file.index[df_login_file['Login'] == login].tolist()
        if str(df_login_file.loc[index[0]]['Senha']) == str(password):
            return True
        else:
            return False
    else:
        False

#Insere veiculo
def insert_veicle(chassi, fabricante, modelo, ano, alimentacao, cor, acentos, portas, descrição, imagem):
    try:
        df_veicle_file = pd.read_excel('Files\\veicles.xlsx', index_col=0)
        na = df_veicle_file.index[df_veicle_file['Fabricante'].isna() == True].tolist()
        try:
            df_veicle_file.loc[na[0],["Chassi", "Fabricante", "Modelo", "Ano", "Alimetação", "Cor", "Acentos", "Portas", "Descrição", "Imagem", "Status"]] = [chassi, fabricante, modelo, ano, alimentacao, cor, acentos, portas, descrição, imagem, "Disponivel"]
        except IndexError:
            df_veicle_file.loc[len(df_veicle_file),["Chassi", "Fabricante", "Modelo", "Ano", "Alimetação", "Cor", "Acentos", "Portas", "Descrição", "Imagem", "Status"]] = [chassi, fabricante, modelo, ano, alimentacao, cor, acentos, portas, descrição, imagem,  "Disponivel"]
        finally:    
            df_veicle_file.to_excel('Files\\veicles.xlsx')
            return
    except FileNotFoundError:
        df_file_login =  pd.DataFrame(columns=["Chassi", "Fabricante", "Modelo", "Ano", "Alimetação", "Cor", "Acentos", "Portas", "Descrição", "Imagem", "Status"], index=[0])
        df_file_login.to_excel('Files\\veicles.xlsx')
        return 0
    
#insert_veicle('6548658', 'Toyota', 'Corola', '2023', 'Gasolina', 'Prata', '5', '4', 'Completo', "C:\\Users\\yansi\\Pictures\\Saved Pictures\\Captura de tela 2022-03-10 153834.png")

def tree(index_list, all):
    try:
        df_veicle_file = pd.read_excel('Files\\veicles.xlsx', index_col=0)
        nodes = []
        treedata = sg.TreeData()
        sg.set_options(font=("",15))
        if all == True:
            for i in range(0,len(df_veicle_file)):
                nodes.append(["", df_veicle_file.loc[i].values[0], "", df_veicle_file.loc[i].values[0], df_veicle_file.loc[i].values[1], df_veicle_file.loc[i].values[2], df_veicle_file.loc[i].values[3], df_veicle_file.loc[i].values[4],df_veicle_file.loc[i].values[5],df_veicle_file.loc[i].values[6],df_veicle_file.loc[i].values[7],df_veicle_file.loc[i].values[8], df_veicle_file.loc[i].values[10]])
            for row in nodes:
                ima= bytes(df_veicle_file.loc[i].values[9], encoding='utf-8')
                treedata.Insert( row[0], row[1], row[2], row[3:], icon=ima)
            return treedata
        else:
            for i in index_list:
                nodes.append(["", df_veicle_file.loc[i].values[0], "", df_veicle_file.loc[i].values[0], df_veicle_file.loc[i].values[1], df_veicle_file.loc[i].values[2], df_veicle_file.loc[i].values[3], df_veicle_file.loc[i].values[4],df_veicle_file.loc[i].values[5],df_veicle_file.loc[i].values[6],df_veicle_file.loc[i].values[7],df_veicle_file.loc[i].values[8], df_veicle_file.loc[i].values[10]])
            for row in nodes:
                ima= bytes(df_veicle_file.loc[i].values[9], encoding='utf-8')
                treedata.Insert( row[0], row[1], row[2], row[3:], icon=ima)
            return treedata

    except FileNotFoundError:
        return FileNotFoundError

def table(index_list, r=False):
    try:
        sg.set_options(font=("", 15))
        headings =["Chassi", "Fabricante", "Modelo", "Ano", "Alimetação", "Cor", "Acentos", "Portas", "Descrição", "Status"]
        df_veicle_file = pd.read_excel('Files\\veicles.xlsx', index_col=0)
        rows=[]
        ima=[]
        for i in index_list:
            rows.append([df_veicle_file.loc[i].values[0], df_veicle_file.loc[i].values[1], df_veicle_file.loc[i].values[2], df_veicle_file.loc[i].values[3], df_veicle_file.loc[i].values[4],df_veicle_file.loc[i].values[5],df_veicle_file.loc[i].values[6],df_veicle_file.loc[i].values[7],df_veicle_file.loc[i].values[8], df_veicle_file.loc[i].values[10]])
            ima.append(bytes(df_veicle_file.loc[i].values[9], encoding='utf-8'))
        tb = sg.Table(values=rows, headings=headings,
        display_row_numbers=False,
        justification='center', key='-TABLE-',
        selected_row_colors='white on green',
        enable_events=True,
        expand_x=True,
        expand_y=True,
        enable_click_events=True)
        if r == True:
            return rows
        else:
            return tb
    except FileNotFoundError:
        return FileNotFoundError

def buscar_veiculo(string):
    try:
        df_veicle_file = pd.read_excel('Files\\veicles.xlsx', index_col=0)
        list = []
        for column in df_veicle_file.columns:
            if column != "Imagem":
                veiculo = df_veicle_file.index[df_veicle_file[column].astype(str).str.contains(string, case=False, regex=False)].tolist()
                if veiculo != []:
                    for v in veiculo:
                        if v not in list:
                            list.append(v)
        return list
    except FileNotFoundError:
        return FileNotFoundError