def opcion_1(ruta):
    palabras = input("Ingrese las palabras para contar entre contactos: ").lower().split()
    guardado = input("Ingrese el archivo destino para guardar el reporte: ")
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

print(opcion_1("Chat_de_Android_de_Friends.txt"))