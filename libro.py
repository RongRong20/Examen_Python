'''Crea una clase Libro en un fichero libro.py que tenga un campo autor, un campo titulo
y un campo anyo con estos nombres.'''

class Libro:
    def __init__(self,autor,titulo,anyo):
        self.__autor = autor
        self.__titulo = titulo
        self.__anyo = anyo