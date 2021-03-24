
'''Crea una funcion llamada get_list que reciba el nombre de un fichero de palabras y devuelva
un diccionario donde la clave de cada elemento sea un numero 1, 2, 3 y el valor sea una lista
con las palabras del fichero que tienen esa longitud. Si una palabra aparece repetida, solo se
tendra en cuenta una. En cada lınea del fichero puede haber mas de una palabra. Si se le
pasa un fichero que no tiene ninguna palabra, la funcion emitira una excepcion ValueError
indicando que el fichero esta vacıo.'''

def get_list(nom):
    f = open(nom, mode="rt", encoding="utf-8")
    texto = f.read()
    
    a = texto.split("\n")
    b =[]
    for x in a:
        print(x,"x")
        b.append(x.split(","))
    print(b,"b")
    print(a,"a")
    

    f.close()
get_list("examen.txt")
    