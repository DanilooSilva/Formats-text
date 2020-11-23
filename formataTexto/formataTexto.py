class FormataTexto(object):
    def __init__(self, texto, formatacao='Titulo'):
        self.__texto = texto
        self.__formatacao = formatacao
    
    def __str__(self):
        return self.__getFormatar()
    
    def __getFormatar(self):
        if self.__formatacao == 'Titulo':
            return self.__texto.title()
        elif self.__formatacao == 'lower':
            return self.__texto.lower()
        else:
            return self.__texto.upper()


