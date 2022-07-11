# VERSÍCULOS DIÁRIOS EM PYTHON

![dayle_verse](dayle_verse.png)
### SOBRE O APP VERSÍCULOS DIÁRIOS EM PYTHON

**Versículos Diários em Python**, assim como o nome sugere, é um aplicativo que funciona como widget que mostra um versículo diferente a cada dia.

### COMO INSTALAR O APP VERSÍCULOS DIÁRIOS EM PYTHON

O primeiro requisito é ter o python em seu computador. Instale-o de acordo com seu computador usando o link [python.org](https://www.python.org/).

Em seguida certifique-se de que  tenha o git instalado. O Git é muito útil e você vai utilizá-lo muito. Instale-o neste link [https://git-scm.com/book/pt-pt/v2/Come%C3%A7ando-Instalar-o-Git](https://git-scm.com/book/pt-pt/v2/Come%C3%A7ando-Instalar-o-Git).

Em seguida, no terminal ou prompt de comandos, clone o meu código:

~~~
git clone https://github.com/elizeubarbosaabreu/Versiculo-do-Dia
~~~

Navegue até o diretório baixado pelo comando anterior:

~~~
cd VersiculoDoDia
~~~

Agora crie um ambiente de desenvolvimento. Se estiver no Linux ou MAC substitua 'python' por 'python3' no comando abaixo:

~~~
python -m venv .venv
~~~

Agora se estiver no Windows, ative o ambiente de desenvolvimento com o comando:

~~~
source .venv\Script\activate.bat 
~~~

Atenção: Se estiver usando Linux ou MAC, você deverá usar o comando abaixo para ativar o ambiente de desenvolvimento:

~~~
source .venv/bin/activate
~~~

Agora instale os requerimentos:

~~~
pip install -r requirements.txt
~~~

Teste com o comando:

~~~
python app.py
~~~

### Como usar o app?

Você criar um link, atalho apontado para o python do ambiente de desenvolvimento e o app.py ou usar o pyinstaller para gerar um software. (Veja como aqui [https://pyinstaller.org/en/stable/](https://pyinstaller.org/en/stable/):
No meu caso, que uso Linux utilizei o Alacarte e criei um link apontando para os diretórios: 
~~~
/home/elizeu/Desktop/VersiculoDoDia/.venv/bin/python3 /home/elizeu/Desktop/VersiculoDoDia/app.py
~~~

Lembre-se: Este é o caminho no meu computador, onde o arquivo está no Desktop e o sistema operacional é Linux.




