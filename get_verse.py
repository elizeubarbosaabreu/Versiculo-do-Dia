import requests
from bs4 import BeautifulSoup

def gerar_versiculo():
    try:
        # requisição da url
        url=f"https://www.bibliaonline.com.br/acf"
        page = requests.get(url)

        # webscrapping com beautifulsoup4
        soup = BeautifulSoup(page.text, 'html.parser')
        text = soup.find_all('article')[0]
        texto = text.get_text().replace('Compartilhar Criar ImagemBíblias são mais de 150 bíblias disponíveisAlmeida Revista e AtualizadaNova Versão TransformadoraNova Almeida AtualizadaAlmeida Revista e CorrigidaNova Versão InternacionalVersão CatólicaAlmeida Corrigida FielKing James VersionReina ValeraOutras Bíblias', '')\
        .replace('Versículos Diários', '').replace('Compartilhar Criar Imagem', '\n').split('\n')
        return texto[0]
        
    except:
        return 'Aconteceu algum erro durante a requisição na internet. \nVerifique sua conexão e tente novamente!!!'

if __name__ == "__main()__":
    print(gerar_versiculo())