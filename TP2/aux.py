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


