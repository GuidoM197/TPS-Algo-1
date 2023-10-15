from random import choice, choices

def recoleccion_de_datos(ruta): # Crea un diccionario que va juntando las palabras y las siguientes con sus ocurrencias.
    """
    Se lee linea por linea identificando los contactos y los mensajes que manda cada uno, luego de esto devuelve un diccionario
    con las palabras que utlizaron y sus ocurrencias.
    """
    
    res = {}

    with open(ruta) as f:

        for linea in f:
            mensaje = linea.lower().split()
            contacto = mensaje[3]
            mensaje = mensaje[4:]

            if "<multimedia" in mensaje[0]: #No salta a la proxima iteracion, corregir!
                continue

            if ":" in contacto:
                contacto = contacto[0].upper() + contacto[1:].rstrip(":")
                res[contacto] = res.get(contacto, {})
            else:
                continue
            
            count = 0
            for palabra in mensaje:

                res[contacto][palabra] = res[contacto].get(palabra, {}) # AGrego la palabra donde estoy parado

                count += 1

                if count < len(mensaje):
                    mensaje_siguiente = mensaje[count]

                if not mensaje_siguiente in res[contacto][palabra] and mensaje_siguiente != palabra:
                    res[contacto][palabra][mensaje_siguiente] = res[contacto][palabra].get(mensaje_siguiente, 0) + 1 #Agrego la palabra siguiente y le sumo su primera aparicion

                if mensaje_siguiente in res[contacto][palabra] and mensaje_siguiente != palabra:
                    res[contacto][palabra][mensaje_siguiente] += 1
                
        return res

def selector_de_palabras(diccionario, contacto):
    """
    Recibe el diccionario de la funcion de "recoleccion_de_datos" y un contacto, luego filtra en base al contacto pasado para utilizar unicamente
    sus palabras y asi generar un mensaje pseudo-aleatorio del mismo.
    """

    lista = []
    peso = []
    palabra_final = []

    for nombre in diccionario.keys():
        if nombre != contacto: continue

        for palabra in diccionario[nombre]:
            lista.append(palabra)
        
        while True:

            palabra_actual = choice(lista)

            palabra_final.append(palabra_actual)
            lista.clear()
            peso.clear()

            for palabras, ocurrencias in diccionario[nombre][palabra_actual].items():
                if palabras != "fin de texto":
                    lista.append(palabras)
                    peso.append(ocurrencias)                    

                if palabras == "fin de texto":
                    lista.append(".")

            
            if peso == [] or palabra_actual == ".": 
                lista.remove(".")
                break

            palabra_actual = choices(lista, peso, k=1) #k=1 para que solo devuelva 1 puesto, el mas grande (boca).


    return " ".join(palabra_final)

def mostrar_contactos(diccionario):
    for i, contacto in enumerate(diccionario.keys()):
        print(i, "-" ,contacto)

def op2(diccionario, contacto):
    print(selector_de_palabras(diccionario, contacto))
            
            
#op2("ejemplo.txt")