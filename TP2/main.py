import logica

def main():

    chat = input("Ingrese la ruta de un archivo de chat: ")
    datos = logica.recoleccion_de_datos(chat)

    print("Bienvendio!")
    print("1) Busqueda de palabras.")
    print("2) Generar un mensaje pseudo-aleatorio.")
    print("3) Salir.")

    opcion = input("Ingrese una de las siguentes opciones porfavor: ")

    if opcion == "1":
        palabras = input("Ingrese las palabras para contar entre contactos: ")
        guardado = input("Ingrese el archivo destino para guardar el reporte: ")
        logica.opcion_1(chat, palabras, guardado)

    if opcion == "2":
        logica.mostrar_contactos(datos)

        while True:

            contacto = input("ngrese el contacto para generar el mensaje: ")
            contacto = logica.validador_de_entrada(contacto, datos)

            if contacto == None: 
                print("Coloque un contacto valido.")
                continue

            palabra_aleatoria = logica.generador_de_palabras(datos, contacto)

            print(f"{contacto}: {palabra_aleatoria}")

            break



main()