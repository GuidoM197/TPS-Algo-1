from cola import Cola
from flood import _cambiar_color

def busqueda_mayor_ocurrencia_adyacentes(matriz):
    cola = Cola()
    cola.encolar((0, 0))
    vistados = set()
    colores_posibles = encontrar_posibles_colores(matriz, vistados)
    

    return colores_posibles


def encontrar_posibles_colores(matriz, visitados):
    cola = Cola()
    cola.encolar((1, 0))
    cola.encolar((0, 1))
    posibles = set() 
    while not cola.esta_vacia():
        i, j = cola.desencolar()

        if matriz[0][0] != matriz[i][j]:
            posibles.add(matriz[i][j])

        encolar_posibles_movimientos(matriz, i, j, cola, visitados)

    return list(posibles) 


def encolar_posibles_movimientos(matriz, i, j, cola, visitados):
    if en_rango(matriz, i+1, j) and ((i+1, j) not in visitados):
        cola.encolar((i+1, j))

    if en_rango(matriz, i, j+1) and ((i, j+1) not in visitados):
        cola.encolar((i, j+1))

    if en_rango(matriz, i-1, j) and ((i-1, j) not in visitados):
        cola.encolar((i-1, j))

    if en_rango(matriz, i, j-1) and ((i, j-1) not in visitados):
        cola.encolar((i, j-1))


def en_rango(matriz, i, j):
    en_rango_i = i >= 0 and i < len(matriz) 
    en_rango_j = j >= 0 and j < len(matriz[0])
    return en_rango_i and en_rango_j


# def busqueda_mayor_ocurrencia(matriz, diccionario):
#     visitados = set()
    
#     color = matriz[1][0]
#     _busqueda_mayor_ocurrencia(matriz, diccionario, 1, 0, color, visitados)
#     color = matriz[0][1]
#     _busqueda_mayor_ocurrencia(matriz, diccionario, 0, 1, color, visitados)


# def _busqueda_mayor_ocurrencia(matriz, diccionario, i, j, color, visitados):
#     if matriz[i][j] != color: return
    
#     if (matriz[i][j] != matriz[0][0]) and ((i, j) not in visitados): #Compruebo no estar teniendo como posibilidad el color base
#         visitados.add((i, j))
#         diccionario[color] = diccionario.get(color, 0) + 1 #Agrego el color y la cantidad que hay adyacentes

#         if ((i - 1) > 0) and ((i-1, j) not in visitados) and matriz[i-1][j] == color:
#             diccionario[color] += 1
#         #    _busqueda_mayor_ocurrencia(matriz, diccionario, i-1, j, color, visitados)

#         if ((i + 1) < len(matriz)) and ((i+1, j) not in visitados) and matriz[i+1][j] == color:
#             diccionario[color] += 1
#         #    _busqueda_mayor_ocurrencia(matriz, diccionario, i+1, j, color, visitados)

#         if ((j - 1) > 0) and ((i, j-1) not in visitados) and matriz[i][j-1] == color:
#             diccionario[color] += 1
#         #    _busqueda_mayor_ocurrencia(matriz, diccionario, i, j-1, color, visitados)
        
#         if ((j + 1) < len(matriz[0])) and ((i, j+1) not in visitados) and matriz[i][j+1] == color:
#             diccionario[color] += 1
#         #    _busqueda_mayor_ocurrencia(matriz, diccionario, i, j+1, color, visitados)

matriz = [[1,0,1,2],
          [2,0,2,1],
          [2,0,1,3],
          [1,4,4,4]] 


# dic = {}

# def busqueda_mejor_mov(matriz):
#     diccionario = {}
#     visitados = set()
#     posibles_colores = set()

#     for fil in range(len(matriz)):
#         for col in range(len(matriz[0])):
#             if matriz[fil][col] != matriz[0][0]:
#                 posibles_colores.add((fil, col))
#                 break
    
#     for posible_color in posibles_colores:
#         i, j = posible_color
#         _busqueda_mayor_ocurrencia(matriz, diccionario, i, j, matriz[i][j], visitados)
    
#     return diccionario

def esta_completado(matriz):

    for i in matriz:
        for j in i:
            if j != matriz[0][0]: return False
    return True

def _calcular_movimientos(matriz):

    #Parte 4: tu código acá...
    copia = matriz.copy()
    max_movimientos = 0
    pasos_aux = Cola()

    while not esta_completado(copia):

        mejor_mov = busqueda_mejor_mov(copia)
        _cambiar_color(copia, 0, 0, mejor_mov, copia[0][0])
        max_movimientos += 1
        pasos_aux.encolar(mejor_mov)

    
    return max_movimientos, pasos_aux

print(busqueda_mejor_mov(matriz))