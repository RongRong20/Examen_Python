'''Crea tambi´en una clase Autor en un fichero autor.py
que tenga un campo id_autor, un campo nombre y un campo apellido'''

class Autor:
    def __init__(self,id, nom, apellido):
        self.__id_autor = id
        self.__nombre = nom
        self.__apellido = apellido