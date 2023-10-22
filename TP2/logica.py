from random import choice, choices

def recoleccion_de_datos(ruta): # Crea un diccionario que va juntando las palabras y las siguientes con sus ocurrencias.
    """
    Se lee linea por linea identificando los contactos y los mensajes que manda cada uno, luego de esto devuelve un diccionario
    con las palabras que utlizaron y sus ocurrencias.
    """
    
    res = {}

    try:
        with open(ruta) as f:

            for linea in f:
                mensaje = linea.lower().split()
                contacto = mensaje[3]
                mensaje = mensaje[4:]

                if "<multimedia" in mensaje: continue

                if ":" in contacto:
                    contacto = contacto[0].upper() + contacto[1:].rstrip(":")
                    res[contacto] = res.get(contacto, {})
                else:
                    continue

                count = 1
                for palabra in mensaje:

                    res[contacto][palabra] = res[contacto].get(palabra, {}) # Agrego la palabra donde estoy parado

                    if count < len(mensaje):
                        mensaje_siguiente = mensaje[count]

                    if count == len(mensaje):
                        mensaje_siguiente = "fin de texto" # Identifica cuando corta el texto

                    if mensaje_siguiente == "fin de texto" and mensaje_siguiente in res[contacto][palabra]: continue

                    if mensaje_siguiente in res[contacto][palabra] and mensaje_siguiente != palabra:
                        res[contacto][palabra][mensaje_siguiente] += 1

                    if not mensaje_siguiente in res[contacto][palabra] and mensaje_siguiente != palabra:
                        res[contacto][palabra][mensaje_siguiente] = res[contacto][palabra].get(mensaje_siguiente, 0) + 1 #Agrego la palabra siguiente y le sumo su primera aparicion

                    count += 1

            return res
        
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return False

def recoleccion_de_palabras(diccionario, persona, palabras, linea):
    """
    Genera un diccionario con el nombre de las personas y las veces que repitieron cada palabra
    """

    if ":" in persona:
        persona = persona[0].upper() + persona[1:].rstrip(":")
        diccionario[persona] = diccionario.get(persona, {})

        for palabra in palabras:
            diccionario[persona][palabra] = diccionario[persona].get(palabra, 0)
            if palabra in linea:
                diccionario[persona][palabra] += 1

def opcion_1(ruta, palabras, guardado): # Ejecuta la primera opción.
    """
    Lee el archivo y genera un diccionario con todas las palabras y las veces que se repitieron, como "key" lleva el nombre del contacto
    para asi identificar las veces que el contacto repitio las palabras.
    """
    res = {}
    palabras = palabras.lower().split()

    try:
        with open(ruta) as origen, open(guardado, "w") as destino:
            next(origen) #Salteo directamente la primera porque es un mensaje predeterminado de Whatsapp

            for linea in origen:
                mensaje = linea.lower().split()
                persona = mensaje[3]

                recoleccion_de_palabras(res, persona, palabras, mensaje)

            for contacto in res.keys():
                for i, j in res[contacto].items():
                    destino.write(f"{contacto}, {i}, {j}\n")

            print("Reporte generado!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")

def selector_de_palabras(lista, diccionario, nombre):
    """
    Se le pasa una lista con las palabras que dice la persona seleccionada, las separa, busca y cuenta, asi les da un peso
    segun la cantidad de veces que se repitieron, luego de esto las mete en otra lista llamada "frase_final".
    """
    peso = []
    frase_final = []

    while True:

        palabra_actual = choice(lista)

        frase_final.append(palabra_actual)
        lista.clear()
        peso.clear() # Limpio las listas para que no se mezclen los valores anteriormente establecidos.

        if len(frase_final) == 10: break

        for palabras, ocurrencias in diccionario[nombre][palabra_actual].items():
            if palabras == "fin de texto": break
            lista.append(palabras)
            peso.append(ocurrencias)

        if peso == []: break

        palabra_actual = choices(lista, peso, k=1) # k=1 para que solo devuelva 1 puesto, el mas grande (boca).

    return frase_final

def opcion_2(diccionario, contacto):
    """
    Recibe el diccionario de la funcion de "recoleccion_de_datos" y un contacto, luego filtra en base al contacto pasado para utilizar unicamente
    sus palabras y asi generar un mensaje pseudo-aleatorio del mismo.
    """

    lista = []

    for nombre in diccionario.keys():
        if nombre != contacto: continue

        for palabra in diccionario[nombre]:
            lista.append(palabra)
        
        frase_final = selector_de_palabras(lista, diccionario, nombre)

    return " ".join(frase_final)

def mostrar_contactos(diccionario):

    for i, contacto in enumerate(diccionario.keys()):
        print(i, "-" ,contacto)

def validador_de_entrada(cadena, diccionario):
    try:
        for i, j in enumerate(diccionario.keys()):
            if cadena == str(i): return j

    except TypeError as msg_error:
        print(f"TypeError: {msg_error}")

def main():

    while True:

        chat = input("Ingrese la ruta de un archivo de chat: ")
        datos = recoleccion_de_datos(chat)

        if datos == False: continue

        break

    while True:

        print("Bienvenido!")
        print("1) Busqueda de palabras.")
        print("2) Generar un mensaje pseudo-aleatorio.")
        print("3) Salir.")

        opcion = input("Ingrese una de las siguentes opciones porfavor: ")

        if opcion == "1":
            palabras = input("Ingrese una oracion para contar las palabras en ella: ")
            guardado = input("Ingrese el archivo destino para guardar el reporte: ")
            opcion_1(chat, palabras, guardado)

        if opcion == "2":
            mostrar_contactos(datos)

            while True:

                contacto = input("Ingrese el contacto para generar el mensaje: ")
                contacto = validador_de_entrada(contacto, datos)

                if contacto == None: 
                    print("Coloque un contacto valido.")
                    continue

                palabra_aleatoria = opcion_2(datos, contacto)

                print(f"{contacto}: {palabra_aleatoria}")

                break

        if opcion == "3":
            print("Hasta luego!", end ="")
            break

main()