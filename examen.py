
'''Crea una funcion llamada get_list que reciba el nombre de un fichero de palabras y devuelva
un diccionario donde la clave de cada elemento sea un numero 1, 2, 3 y el valor sea una lista
con las palabras del fichero que tienen esa longitud. Si una palabra aparece repetida, solo se
tendra en cuenta una. En cada lınea del fichero puede haber mas de una palabra. Si se le
pasa un fichero que no tiene ninguna palabra, la funcion emitira una excepcion ValueError
indicando que el fichero esta vacıo.'''

from libro import Libro
from autor import Autor

def get_list(nom):
    f = open(nom, mode="rt", encoding="utf-8")
    
    texto = f.read()
    if texto is None or "":
        raise ValueError("el fichero esta vacio")
    else:

        a = texto.split("\n")
        b =[]
        dic = {}
        j = []
        for x in a:
            #print(x,"x")
            b.append(x.split(","))
        #print(b,"b")
        #print(a,"a")
        g = 0
    
        for s in b:
            if len(s) >=2:
                for d in s:
                    #print(d,"d")
                    #print(len(d),"lend")
                    j.append(d)
                    if len(d)> g:
                        g = len(d)
        #print(g,"g")
        for h in range(g+1):
            dic.update({h:""})
        #print(dic,"dic")
        for u in j:
            for y in j:
                if u == y:
                    j.remove(y)
            j.append(u)
    
        for l in j:
                    
            if dic[len(l)] != l:
                dic[len(l)]= dic[len(l)]+"  "+l
        #print(j,"j")
        #print(dic,"dic2")
        return dic


    f.close()

di = get_list("examen.txt")
print(di)

'''En el main de examen.py se crear´a una lista de varios objetos Libro y se llamar´a a
una funci´on mas_antiguos pas´andole esta lista y un a˜no. La funci´on devolver´a una lista
de los t´ıtulos de libros (´unicamente el t´ıtulo) cuyo a˜no es igual o anterior al pasado
por par´ametro. Si se le pasa un a˜no menor que 1900 o mayor que 2021, se emitir´a una
excepci´on ValueError indicando que el a˜no no es v´alido.'''
lista = []
q = Libro(1,"Payaso",1998)
lista.append({q.get_titulo():q.get_anyo()})
w = Libro(1,"Bomba", 2000)
lista.append({w.get_titulo():w.get_anyo()})
e = Libro(2, "La casa de los espíritus", 2010)
lista.append({e.get_titulo():e.get_anyo()})
r = Libro(3, "Habia una vez", 2003)
lista.append({r.get_titulo():r.get_anyo()})
print(lista)
d = []
def mas_antiguos(a):
    if a>2021 or a<1900:
        raise ValueError("el año introducido es mayor de 2021 o menor de 1900")
    else:
        for x in lista:

            if 


mas_antiguos(1999)

    