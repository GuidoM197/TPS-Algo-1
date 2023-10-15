from random import choice, choices
import os

print(os.listdir())

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