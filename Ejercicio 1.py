

def process_class():
    """Esta función lee un fichero csv  con notas de los alumnos y 
    las almacena.
        -Parámetros:
            -Fichero = str con la ruta del fichero (.csv) a abrir
        -Salida:
            -No tiene
    """
    
    Fichero = ('class.csv')
    file = open ('class.csv', 'r')
    dos = [0,1]
    patron = [1,3,5,7,9,11] 
    patron2 = [2,3,4,5,6,7]
    lineas = file.read() 
    lineas=lineas.split("\n") 
    diccionario = [] 
    cabecera= lineas[0].split(",") 
    lineas.pop(0) 
    for i in range(len(lineas)):
        Fila = lineas[i].split('"')
        alumno = {}
        nombre = Fila[0].split(",")
        for u in dos:
            alumno[cabecera[u]] = nombre[u]
        for k,j in zip(patron,patron2): 
            alumno[cabecera[j]] = Fila[k]
        diccionario.append(alumno)
    print(diccionario)
    file.close
process_class()

    




    