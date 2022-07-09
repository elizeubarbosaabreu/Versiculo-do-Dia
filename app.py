import requests
from bs4 import BeautifulSoup
import PySimpleGUI as sg


# requisição da url
url=f"https://www.bibliaonline.com.br/acf"
page = requests.get(url)

# webscrapping com beautifulsoup4
soup = BeautifulSoup(page.text, 'html.parser')
text = soup.find_all('article')[0]
texto = text.get_text().replace('Compartilhar Criar ImagemBíblias são mais de 150 bíblias disponíveisAlmeida Revista e AtualizadaNova Versão TransformadoraNova Almeida AtualizadaAlmeida Revista e CorrigidaNova Versão InternacionalVersão CatólicaAlmeida Corrigida FielKing James VersionReina ValeraOutras Bíblias', '')\
.replace('Versículos Diários', '').replace('Compartilhar Criar Imagem', '\n').split('\n')


# pySimpleGUI
sg.theme('Reddit')
# Define o Layout/ Conteúdo da Tela
layout = [[sg.T(texto[0], font=('Arial', 12), size=(40, 2))]]

# Desenha a tela
window = sg.Window('Versículo do Dia', layout)

# Mostra a interação com o usuário em um loop
while True:
    event, values = window.read()
   
    if event == sg.WINDOW_CLOSED:
        break    

# Fecha a tela
window.close()
