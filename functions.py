import pandas as pd

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