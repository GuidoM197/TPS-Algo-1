matriz = [[" "," "," ","X"],
          [" "," ","X"," "],
          [" ","X"," "," "],
          ["X"," "," "," "]]

def verificar_contiguos(lista, ficha):

    if len(lista) == 4:
        for i in range(len(lista)):
            if i+3>len(lista)-1:
                break

            if son_cuatro_contiguos(lista, i, ficha): return True

            if son_cuatro_contiguos(lista, i, ficha): return True
        
    return False

def son_cuatro_contiguos(lista, i, ficha):
    return lista[i] == ficha and lista[i+1] == ficha and lista[i+2] == ficha and lista[i+3] == ficha