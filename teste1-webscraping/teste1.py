import requests
from bs4 import BeautifulSoup
import zipfile
import os

url = 'https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude'
response = requests.get(url)
content = BeautifulSoup(response.text, 'html.parser')
all_urls = content.find_all('a')

# Encontra os arquivos requisitados e realiza o download diretamente para a pasta "anexos"
def download(): 
    for url in all_urls:
        try:
            if 'Anexo' in url['href']:
                #print(url['href'])
                file_url = url['href']

                file_name = file_url.split('/')[-1]
                #print(file_name)
                #             
                file_response = requests.get(file_url)

                with open ('teste1-webscraping/anexos/' + file_name, 'wb') as f:

                    f.write(file_response.content)

        except Exception as e:
            print(e)

# Pega todo o conteúdo que está na pasta "anexos" e coloca em um .zip
def zip_directory(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, mode='w') as zipf:
        len_dir_path = len(folder_path)
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, file_path[len_dir_path:])                


download()
zip_directory('teste1-webscraping/anexos/', 'teste1-webscraping/anexos-zip.zip')