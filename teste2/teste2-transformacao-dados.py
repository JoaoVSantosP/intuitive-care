import tabula
from zipfile import ZipFile

# baixar o csv e sem seguida, zipar
def extractPDF(pdf_path, pages): 
    dfs = tabula.read_pdf(pdf_path, pages=pages)
    i = 0
    for df in dfs:       
        if ('PROCEDIMENTO' in df.iloc[0].to_string()) and i == 0:            
            
            # df = df.rename(columns={'OD':'Seg. Odontológica'}) 
            # df = df.rename(columns={'AMB':'Seg. Ambulatorial'})
            # df['OD'] = df['OD'].replace('OD','Seg. Odontológica')
            # df['Seg. Ambulatorial'] = df['Seg. Ambulatorial'].replace('AMB','Seg. Ambulatorial')            
            
            df.to_csv('teste2/' + 'Rol de Procedimentos e Eventos em Saúde' + '.csv ', sep=';', encoding='utf-8', index=False, header=True)
            i = i + 1

        else:
            # df['OD'] = df['OD'].replace('OD','Seg. Odontológica')
            # df['AMB'] = df['AMB'].replace('AMB','Seg. Ambulatorial')
            
            df.to_csv('teste2/' + 'Rol de Procedimentos e Eventos em Saúde' + '.csv ', sep=';', mode='a', encoding='utf-8', index=False, header=False)
    zipCsv()


def zipCsv():
    with ZipFile('teste2/Teste_{Joao_Victor}.zip', 'w') as zipObj: #Cria um arquivo .zip
        zipObj.write('teste2/' + 'Rol de Procedimentos e Eventos em Saúde' + '.csv')


pages = '3-200'
pdf_path = 'https://www.gov.br/ans/pt-br/arquivos/assuntos/consumidor/o-que-seu-plano-deve-cobrir/Anexo_I_Rol_2021RN_465.2021_RN473_RN478_RN480_RN513_RN536.pdf'

extractPDF(pdf_path, pages)