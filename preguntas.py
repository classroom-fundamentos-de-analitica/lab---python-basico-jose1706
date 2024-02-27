"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
datos = []
with open("data.csv", "r") as archivo_datos:
    lector = csv.reader(archivo_datos, delimiter="\t")
    for fila in lector:
        datos.append(fila)

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    R1 = 0
    for i in range(len(datos)):
        R1 += int(datos[i][1])

    return R1


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    dic2 = {}
    for i in range(len(datos)):
        dic2[datos[i][0]] = dic2.get(datos[i][0], 0) + 1
 
    return list(sorted(dic2.items()))


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    dic3 = {}
    for i in range(len(datos)):
        dic3[datos[i][0]] = dic3.get(datos[i][0], 0) + int(datos[i][1])
 
    return list(sorted(dic3.items()))


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    fecha = [z[2].split("-") for z in datos]
    dic4 = {}
    for i in range(len(fecha)):
        dic4[fecha[i][1]] = dic4.get(fecha[i][1], 0) + 1
 
    return list(sorted(dic4.items()))


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    dic5 = {}
    for i in range(len(datos)):
        if not (datos[i][0] in dic5):
            dic5[datos[i][0]] = [datos[i][0], int(datos[i][1]), int(datos[i][1])]
        else:
            if dic5[datos[i][0]][1] < int(datos[i][1]):
                dic5[datos[i][0]][1] = int(datos[i][1])
            elif dic5[datos[i][0]][2] > int(datos[i][1]):
                dic5[datos[i][0]][2] = int(datos[i][1])
    salida = sorted(dic5.values())
    lista_de_tuplas = [tuple(sublista) for sublista in salida]

    return lista_de_tuplas

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """

    valores = {}

    for fila in datos:
        columna_5 = fila[4]  
        pares = columna_5.split(',')  
    
        for par in pares:
            clave, valor_str = par.split(':') 
            valor = int(valor_str)  
            if clave in valores:
                valores[clave] = (
                    min(valores[clave][0], valor),  # Minimo
                    max(valores[clave][1], valor)   # Maximo
                    )
            else:
                valores[clave] = (valor, valor)

    resultado = [(clave, min_max[0], min_max[1]) for clave, min_max in valores.items()]
    resultado.sort()


    '''
    dic_datos1 = [z[4].split(",") for z in datos]
    dd2 = {}
    for elm in dic_datos1:
        for i in range(len(elm)):
            clave, valor = elm[i].split(":")
            if clave not in dd2:
                dd2[clave] = [clave, valor, valor]
            else:
                if dd2[clave][1] > valor:
                    dd2[clave][1] = valor
                elif dd2[clave][2] < valor:
                    dd2[clave][2] = valor
    salida1 = sorted(dd2.values())
    lista_de_tuplas1 = [tuple(sublista) for sublista in salida1]
    #revisar donde esta el error 
    '''
    return resultado
print(pregunta_06())

def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    dic7 = {}
    for i in range(len(datos)):
        if int(datos[i][1]) not in dic7:
            dic7[int(datos[i][1])] = [datos[i][0]]
        else:
            dic7[int(datos[i][1])] = dic7[int(datos[i][1])]+[datos[i][0]]
 
    return list(sorted(dic7.items()))

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    dic7 = {}
    for i in range(len(datos)):
        if int(datos[i][1]) not in dic7:
            dic7[int(datos[i][1])] = [datos[i][0]]
        else:
            if datos[i][0] in dic7[int(datos[i][1])]:
                continue
            else:
                dic7[int(datos[i][1])] = sorted(dic7[int(datos[i][1])]+[datos[i][0]])
 
    return list(sorted(dic7.items()))

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    dic_datos9 = [z[4].split(",") for z in datos]
    dicc9 = {}
    for elm in dic_datos9:
        for i in range(len(elm)):
            clave, valor = elm[i].split(":")
            dicc9[clave] = dicc9.get(clave, 0) + 1

    return dict(sorted(dicc9.items()))


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    dic10 = [z[4].split(",") for z in datos]
    lis10 = []
    for i in range(len(datos)):
        lis10.append((datos[i][0], sum(1 for x in datos[i][3] if x.isalpha()), len(dic10[i])))

    return lis10


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    list11 = [z[3].split(",") for z in datos]
    dic11 = {}
    for i in range(len(datos)):
        valor = int(datos[i][1])
        for j in range(len(list11[i])):
            dic11[list11[i][j]] = dic11.get(list11[i][j], 0) + valor

    lisO = sorted(dic11.items())
    return dict(lisO)

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    lis11 = [z[4].split(",") for z in datos]
    dic12 = {}
    for i in range(len(datos)):
        clave = datos[i][0]
        suma = 0
        for j in range(len(lis11[i])):
            cl, valor = lis11[i][j].split(":")
            suma += int(valor)
        if clave not in dic12:
            dic12[clave] = suma
        else:
            dic12[clave] = dic12[clave] + suma
    
    return dict(sorted(dic12.items()))
