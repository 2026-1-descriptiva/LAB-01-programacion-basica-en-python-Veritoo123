"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    result = {}

    with open("files/input/data.csv") as file:
        for line in file:
            columns = line.strip().split("\t")

            total = sum(
                int(pair.split(":")[1])
                for pair in columns[4].split(",")
            )

            result[columns[0]] = result.get(columns[0], 0) + total

    return dict(sorted(result.items()))

    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
