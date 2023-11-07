from random import choice, choices

def identificador_de_usuarios(diccionario, mensaje):
    '''
    Identifica los nombres de los contactos y determina hasta cual espacio se movio, este numero lo devuelve para saber cuando empieza el mensaje.
    '''

    nombre = []
    contador = 1
    for palabra in mensaje:

        if ":" in palabra:
            nombre.append(palabra.rstrip(":"))
            persona = " ".join(nombre)
            diccionario[persona] = diccionario.get(persona, {})

            return persona
        
        else:
            nombre.append(palabra)
            contador += 1

def identificador_de_comienzo_de_mensaje(mensaje):
    contador = 0
    for elemento in mensaje:
        if ":" in elemento: return contador
        contador += 1
    return -1

def recolectar_palabras(diccionario, palabra, nombre):

    res = []
    contador_de_palabras = 0
    veces_repetida = 0 # Lo utilizo para identificar si esta en el diccionario pero no esta despues de ninguna palabra.
    res.append(nombre)
    res.append(palabra)

    for i in diccionario[nombre]: 
        if i == palabra and veces_repetida == 0:
            contador_de_palabras += 1
            veces_repetida = 1

        for j in diccionario[nombre][i]:
            if j == palabra: 
                contador_de_palabras += diccionario[nombre][i][j]
                veces_repetida = 1
    
    res.append(str(contador_de_palabras))
    
    return ",".join(res)


def analizador_de_palabras(diccionario, nombre, mensaje):

    count = 1
    for palabra in mensaje:

        diccionario[nombre][palabra] = diccionario[nombre].get(palabra, {}) # Agrego la palabra donde estoy parado

        if count < len(mensaje): mensaje_siguiente = mensaje[count]

        if count == len(mensaje): mensaje_siguiente = "fin de texto" # Identifica cuando corta el texto

        if mensaje_siguiente == "fin de texto" and mensaje_siguiente in diccionario[nombre][palabra]: continue

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
                mensaje = mensaje[3:]

                if "<multimedia" in mensaje: continue

                nombre = identificador_de_usuarios(res, mensaje)

                inicio_del_mensaje = identificador_de_comienzo_de_mensaje(mensaje)

                if inicio_del_mensaje == -1: continue

                mensaje = mensaje[inicio_del_mensaje + 1:]

                analizador_de_palabras(res, nombre, mensaje)

            return res

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
        return False

def opcion_1(diccionario, palabras, guardado): # Ejecuta la primera opción.
    """
    Lee el archivo y genera un diccionario con todas las palabras y las veces que se repitieron, como "key" lleva el nombre del contacto
    para asi identificar las veces que el contacto repitio las palabras.
    """

    palabras = palabras.lower().split()

    try:
        with open(guardado, "w") as destino:
            for palabra in palabras:
                for nombre in diccionario:
                    veces_dichas = recolectar_palabras(diccionario, palabra, nombre)
                    destino.write(f"{veces_dichas} \n")
        
        print("Reporte generado!")

    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")

def selector_de_palabras(lista, diccionario, nombre):
    """
    Se le pasa una lista con las palabras que utiliza la persona seleccionada, luego las separa, busca y cuenta, asi les da un peso
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

def validador_de_contacto(numero, diccionario):
    """
    Los contactos en pantalla se muestan con numeros Ej: (0 - Monica, 1 - Ross, etc) asi que de esta forma se detecta si ingreso un
    numero valido, osea, que represente a algun contacto. De ser asi, devuelve el contacto.
    """
    try:
        for indice, contacto in enumerate(diccionario.keys()):
            if numero == str(indice): return contacto

    except TypeError as msg_error:
        print(f"TypeError: {msg_error}")

def validar_csv(entrada): return entrada[len(entrada) - 4:len(entrada)] == ".csv"
