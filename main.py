from formataTexto import FormataTexto
from interface import Windows
import PySimpleGUI as sg

if __name__ == '__main__':
    janela = Windows().gerarTela()
    while True:
        eventos, valores = janela.read()

        if eventos in (sg.WIN_CLOSED, 'Cancelar'):
            break
        if eventos == 'Limpar':
            janela['saida'].update('')
            janela['texto'].update('')
            janela['Titulo'].update(value=False)
            janela['UPPER'].update(value=False)
            janela['lower'].update(value=False)
        elif eventos == 'Formatar' and valores['Titulo']:
            txt = FormataTexto(valores['texto'], 'Titulo')
            sg.popup_ok(f'Texto Formatado: {txt}, para copiar favor ir até a aba de Sáida')
            print('Texto Formatoda: ')
            print(txt)
        elif eventos == 'Formatar' and valores['UPPER']:
            txt = FormataTexto(valores['texto'], 'UPPER')
            sg.popup_ok(f'Texto Formatado: {txt}, para copiar favor ir até a aba de Sáida')
            print('Texto Formatoda: ')
            print(txt)
        elif eventos == 'Formatar' and valores['lower']:
            txt = FormataTexto(valores['texto'], 'lower')
            sg.popup_ok(f'Texto Formatado: {txt}, para copiar favor ir até a aba de Sáida')
            print('Texto Formatoda: ')
            print(txt)
        else:
            sg.popup_error('ERRO: INFORMAR O TIPO DE FORMATAÇÃO.')
    janela.close()
