import PySimpleGUI as sg

sg.theme('LightBrown2')
def funcao_principal():
    estilizacao = [
        [sg.Text('--EXPONECIAÇÃO--')],
        [sg.Text('base'), sg.Input(key='base')],
        [sg.Text('expoente'), sg.Input(key='expoente')],
        [sg.Text(size=(40, 1), key='texto')],
        [sg.Button('enviar'), sg.Button('sair')]
    ]
    janela = sg.Window('É A POTENCIA').layout(estilizacao)
    while True:
        even,valo = janela.read()
        if even == sg.WINDOW_CLOSED or even == 'sair':
            break
        if even == 'enviar':
            based = int(valo['base'])
            expo = int(valo['expoente'])
            janela['texto'].update(based ** expo)


funcao_principal()