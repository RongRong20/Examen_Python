
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
    dic = {}
    for x in a:
        #print(x,"x")
        b.append(x.split(","))
    #print(b,"b")
    #print(a,"a")
    g = 0
    for s in b:
        if len(s) >=2:
            for d in s:
                print(d,"d")
                print(len(d),"lend")
                if len(d)> g:
                    g = len(d)
    print(g,"g")
    for h in range(g+1):
        dic.update({h:"None"})
    print(dic,"dic")
    for s in b:
        if len(s) >=2:
            for d in s:
                if dic[len(d)] != d:
                    dic[len(d)]= dic[len(d)]+d
    print(dic,"dic2")
                
               
        
                




    f.close()

get_list("examen.txt")
    