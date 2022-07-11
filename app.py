
import PySimpleGUI as sg
from get_verse import gerar_versiculo

# __     __            _            _                 _         ____  _       
# \ \   / /__ _ __ ___(_) ___ _   _| | ___  ___    __| | ___   |  _ \(_) __ _ 
#  \ \ / / _ \ '__/ __| |/ __| | | | |/ _ \/ __|  / _` |/ _ \  | | | | |/ _` |
#   \ V /  __/ |  \__ \ | (__| |_| | | (_) \__ \ | (_| | (_) | | |_| | | (_| |
#    \_/ \___|_|  |___/_|\___|\__,_|_|\___/|___/  \__,_|\___/  |____/|_|\__,_|
#                                                                             
'''
Este aplicativo faz requisição no site https://www.bibliaonline.com.br à procura
um versículo diário e retorna com interface gráfica...

Desenvolvido por Elizeu Barbosa Abreu
'''


# pySimpleGUI
sg.theme('Reddit')
# Define o Layout/ Conteúdo da Tela
layout = [
    [sg.Stretch(),
     sg.T('VERSÍCULO DO DIA',
          font=('Arial', 16)),
     sg.Stretch()],
    [sg.HorizontalSeparator()],
    [sg.Stretch(),
     sg.Text(gerar_versiculo(),
             font=('Arial', 12),
             justification='center',
             size=(30,10)),
     sg.Stretch()]
    ]

# Desenha a tela
window = sg.Window('Versículo do Dia',
                   layout,
                   margins=(0, 0),
                   finalize=True,
                   #keep_on_top=True,
                   #no_titlebar=True,
                   grab_anywhere=True,
                   alpha_channel=0.8,
                   size=(300, 250))

# Mostra a interação com o usuário em um loop
while True:
    event, values = window.read()
   
    if event == sg.WINDOW_CLOSED:
        break    

# Fecha a tela
window.close()
