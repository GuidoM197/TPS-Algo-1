import logica

def mostrar_contactos(diccionario):

    for i, contacto in enumerate(diccionario.keys()):
        print(i, "-" ,contacto)

def main():

    while True:

        chat = input("Ingrese la ruta de un archivo de chat: ")
        datos = logica.recoleccion_de_datos(chat)

        if datos == False: continue

        break

    while True:

        print("")
        print("Bienvenido!")
        print("1) Busqueda de palabras.")
        print("2) Generar un mensaje pseudo-aleatorio.")
        print("3) Salir.")

        opcion = input("Ingrese una de las siguentes opciones porfavor: ")

        if opcion == "1":

                palabras = input("Ingrese una oracion para contar las palabras en ella: ")
                guardado = input("Ingrese el archivo destino para guardar el reporte: ")
                logica.opcion_1(chat, palabras, guardado)

        if opcion == "2":
            mostrar_contactos(datos)

            while True:

                contacto = input("Ingrese el contacto para generar el mensaje: ")
                contacto = logica.validador_de_entrada(contacto, datos)

                if contacto == None: 
                    print("Coloque un contacto valido.")
                    continue

                palabra_aleatoria = logica.opcion_2(datos, contacto)

                print(f"{contacto}: {palabra_aleatoria}")

                break

        if opcion == "3":
            print("Hasta luego!")
            return

main()