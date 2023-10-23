from random import choice, choices

def identificador_de_usuarios(diccionario, mensaje):

    persona = mensaje[3]

    if ":" in persona:
        persona = persona.rstrip(":")
        diccionario[persona] = diccionario.get(persona, {})

def contar_palabras(diccionario, mensaje, palabras):

    linea = mensaje[4:]

    for nombre in diccionario.keys():
        persona = mensaje[3]

        for palabra in palabras:

            if persona == nombre + ":":
                diccionario[nombre][palabra] = diccionario[nombre].get(palabra, 0)
                if palabra in linea:
                    diccionario[nombre][palabra] += 1

def analizador_de_palabras(diccionario, mensaje):
    
    for nombre in diccionario.keys():

        count = 1
        for palabra in mensaje:

            diccionario[nombre][palabra] = diccionario[nombre].get(palabra, {}) # Agrego la palabra donde estoy parado

            if count < len(mensaje):
                mensaje_siguiente = mensaje[count]

            if count == len(mensaje):
                mensaje_siguiente = "fin de texto" # Identifica cuando corta el texto

            if mensaje_siguiente == "fin de texto" and mensaje_siguiente in diccionario[nombre][palabra]: continue

            if mensaje_siguiente in diccionario[nombre][palabra] and mensaje_siguiente != palabra:
                diccionario[nombre][palabra][mensaje_siguiente] += 1

            if not mensaje_siguiente in diccionario[nombre][palabra] and mensaje_siguiente != palabra:
                diccionario[nombre][palabra][mensaje_siguiente] = diccionario[nombre][palabra].get(mensaje_siguiente, 0) + 1 #Agrego la palabra siguiente y le sumo su primera aparicion

            count += 1

def recoleccion_de_datos(ruta): # Crea un diccionario que va juntando las palabras y las siguientes con sus ocurrencias.
    """
    Se lee linea por linea identificando los contactos y los mensajes que manda cada uno, luego de esto devuelve un diccionario
    con las palabras que utlizaron y sus ocurrencias.
    """
    
    res = {}

    try:
        with open(ruta) as f:
            next(f)

            for linea in f:
                mensaje = linea.lower().split()

                if "<multimedia" in mensaje: continue

                identificador_de_usuarios(res, mensaje)

                mensaje = mensaje[4:]

                analizador_de_palabras(res, mensaje)

            return res

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return False

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

                identificador_de_usuarios(res, mensaje)

                contar_palabras(res, mensaje, palabras)

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

def validador_de_entrada(numero, diccionario):
    """
    Los contactos en pantalla se muestan con numeros Ej: (0 - Monica, 1 - Ross, etc) asi que de esta forma se detecta si ingreso un
    numero valido, osea, que represente a algun contacto. De ser asi, devuelve el contacto.
    """
    try:
        for indice, contacto in enumerate(diccionario.keys()):
            if numero == str(indice): return contacto

    except TypeError as msg_error:
        print(f"TypeError: {msg_error}")