import cuatro_en_linea

def main():
    
    centinela = True

    while True:

        filas = input("ingrese el alto de su tablero entre 4 y 10: ")
        columnas = input("ingrese el ancho de su tablero entre 4 y 10: ")

        validacion_tablero = cuatro_en_linea.validacion_de_tablero(filas, columnas)

        if validacion_tablero:
            tablero = cuatro_en_linea.crear_tablero(filas, columnas)
            cuatro_en_linea.graficar_tablero(tablero)
            break

    while centinela:
        
        cuatro_en_linea.es_turno_de_x(tablero)
        jugada = input("O presione 's' para salir: ")

        if jugada == "s": return

        ok = cuatro_en_linea.insertar_simbolo(tablero, jugada)

        if ok:
            cuatro_en_linea.graficar_tablero(tablero)
            ganador = cuatro_en_linea.obtener_ganador(tablero)
            tablero_lleno = cuatro_en_linea.tablero_completo(tablero)

            if ganador != " ":
                print(f"El ganador es: " + ganador)
                break

            if tablero_lleno:
                print("No hubo ganador :(")
                break

main()