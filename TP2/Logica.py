from random import choice, choices

def opcion_1(ruta, palabras, guardado):
    """
    Lee el archivo y genera un diccionario con todas las palabras y las veces que se repitieron, como "key" lleva el nombre del contacto
    para asi identificar las veces que el contacto repitio las palabras.
    """

    palabras = palabras.lower().split()
    res = {}

    with open(ruta) as origen, open(guardado, "w") as destino:

        for fila in origen:
            mensaje = fila.lower().split()
            persona = mensaje[3]

            if ":" in persona:
                persona = persona[0].upper() + persona[1:].rstrip(":")
                res[persona] = res.get(persona, {})
            else:
                continue

            for palabra in palabras:
                res[persona][palabra] = res[persona].get(palabra, 0)
                if palabra in mensaje:
                    res[persona][palabra] += 1
                
        for contacto in res.keys(): #Solucion momentanea, ver como intercalar contactos entre palabra y palabra
            for i, j in res[contacto].items():
                destino.write(f"{contacto}, {i}, {j}\n")

def recoleccion_de_datos(ruta): # Crea un diccionario que va juntando las palabras y las siguientes con sus ocurrencias.
    """
    Se lee linea por linea identificando los contactos y los mensajes que manda cada uno, luego de esto devuelve un diccionario
    con las palabras que utlizaron y sus ocurrencias (Salvo las ocurrencias de las palabras iniciales).
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

def generador_de_palabras(diccionario, contacto):
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

