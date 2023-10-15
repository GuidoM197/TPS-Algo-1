from random import choice, choices
import os


def opcion_1(ruta):
    palabras = input("Ingrese las palabras para contar entre contactos: ").lower().split()
    guardado = input("Ingrese el archivo destino para guardar el reporte: ")
    res = {}

    with open(ruta) as origen, open(guardado, "w") as destino:

        for fila in origen:
            mensaje = fila.lower().split()
            mensaje = mensaje[3:]
            persona = mensaje[0]

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

dic = {
    "Guido": {"hola": {"como": 2,
                       "estas?": 3},

            "como": {"andas?": 8,
                     "estaban": 3},

            "estas?": {"fin de texto": 1},         

            "andas?": {"fin de texto": 1},

            "estaban": {"fin de texto": 1}},

    "Doly": {"hola": {"estas?": 2,
                      "queres?": 5},

            "como": {"estas?": 7,
                     "bien": 4},

            "queres?": {"fin de texto": 1},

            "estas?": {"fin de texto": 1},

            "bien": {"fin de texto": 1}},

}

def selector_de_palabras(diccionario, contacto):
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


    print(" ".join(palabra_final))

#l = []
#selector = []
#peso = []
#for nombre in dic.keys():

#    for i in dic["Guido"]:
#        l.append(i)
#    print(l)

#    actual = choice(l)
#    l.clear()

#    for i, j in dic["Guido"][actual].items():
#        l.append(i)
#        peso.append(j)

#    palabra = choices(l, peso, k = 1)[0]

#    print(l)
#    print(peso)
#    print(palabra)

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
            if "<multimedia" in mensaje:
                mensaje = None
                if mensaje == None:
                    continue
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
                    mensaje_siguiente = "fin de texto" #Identifica cuando corta el texto
                
                if mensaje_siguiente == "fin de texto" and mensaje_siguiente in res[contacto][palabra]: continue
                if mensaje_siguiente in res[contacto][palabra] and mensaje_siguiente != palabra:
                    res[contacto][palabra][mensaje_siguiente] += 1
                if not mensaje_siguiente in res[contacto][palabra] and mensaje_siguiente != palabra:
                    res[contacto][palabra][mensaje_siguiente] = res[contacto][palabra].get(mensaje_siguiente, 0) + 1 #Agrego la palabra siguiente y le sumo su primera aparicion
                count += 1
    
        return res
    