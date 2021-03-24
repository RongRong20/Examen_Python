'''Crea una clase Libro en un fichero libro.py que tenga un campo autor, un campo titulo
y un campo anyo con estos nombres.'''

class Libro:
    def __init__(self,autor,titulo,anyo):
        self.__autor = autor
        self.__titulo = titulo
        self.__anyo = anyo

    def get_autor(self):
        return self.__autor
    def get_titulo(self):
        return self.__titulo
    def get_anyo(self):
        return self.__anyo