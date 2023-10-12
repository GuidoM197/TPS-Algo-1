import cuatro_en_linea

def graficar_tablero(tablero):

    indices = []
    separacion = "".ljust(len(tablero[0])*2, "_") + "_"

    for i in range(len(tablero[0])):
        indices.append(str(i))
    print("")

    print("|" + "|".join(indices) + "|")

    print(separacion)

    print("")

    for i in range(len(tablero)):
        print("|" + "|".join(tablero[i]) + "|")

def main():

    while True:

        filas = input("ingrese la cantidad de filas de su tablero: ")
        columnas = input("ingrese la cantidad de columnas de su tablero: ")

        if cuatro_en_linea.validacion_de_tablero(filas, columnas) != False:

            filas, columnas = cuatro_en_linea.validacion_de_tablero(filas, columnas)
            tablero = cuatro_en_linea.crear_tablero(filas, columnas)
            graficar_tablero(tablero)
            break

        continue
            
    while True:
        
        if cuatro_en_linea.es_turno_de_x(tablero):
            print(f"Juega X, ingrese una columna del 0 al {len(tablero[0])-1} : ")
        else:
            print(f"Juega O, ingrese una columna del 0 al {len(tablero[0])-1} : ")

        jugada = input("O ingrese `s` para salir. ")

        jugada = cuatro_en_linea.validacion_de_jugada(jugada)

        if jugada == "s": return

        if jugada == "False": continue
            
        ok = cuatro_en_linea.insertar_simbolo(tablero, jugada)

        if ok:
            graficar_tablero(tablero)
            ganador = cuatro_en_linea.obtener_ganador(tablero)
            tablero_lleno = cuatro_en_linea.tablero_completo(tablero)

            if ganador != " ":
                print(f"El ganador es: {ganador}")
                break

            if tablero_lleno:
                print("No hubo ganador :(")
                break
        
main()