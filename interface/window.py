import PySimpleGUI as sg


class Windows:
    def __init__(self):
        sg.theme('Black')
        self.__layout_entrada = [
            [sg.Text('Texto para Formatação:', size=(20, 1))],
            [sg.InputText(key='texto', size=(40, 1))],
            [
                sg.Radio('Titulo', group_id='tipoFormatacao', size=(12, 1), key='Titulo'), 
                sg.Radio('UPPER', group_id='tipoFormatacao', size=(12, 1), key='UPPER'), 
                sg.Radio('lower', group_id='tipoFormatacao', size=(12, 1), key='lower')
            ]
        ]
        self.__layout_saida = [
            [sg.Text('Texto Formatado:', size=(20, 1))],
            [sg.Output(size=(40, 20), key='saida')],    
        ]
    def gerarTela(self):
        layout = [
            [
                sg.TabGroup(
                    [[
                        sg.Tab('Inicio', self.__layout_entrada), 
                        sg.Tab('Saída', self.__layout_saida)
                    ]]
                )
            ],
            [
                sg.Button('Formatar', size=(15, 1)), 
                sg.Button('Cancelar', size=(15, 1)),
                sg.Button('Limpar', size=(15, 1))
            ]
        ]
        return  sg.Window('Formatação de Texto', layout)
