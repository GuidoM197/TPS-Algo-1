def contar_ocurrencias(palabra, lista):
    indice = 0
    contador = 0
    
    for i in range(len(lista)):
        if palabra == lista[i]:
            contador += 1
            if contador == 1:
                indice = i

    return (indice, contador)

def opcion_2(ruta):
    res = {}

    with open(ruta) as f:

        for linea in f:
            mensaje = linea.lower().split()
            mensaje = mensaje[3:]
            contacto = mensaje[0]

            if "<Multimedia omitido>" in mensaje: continue

            if ":" in contacto:
                contacto = contacto[0].upper() + contacto[1:].rstrip(":")
                res[contacto] = res.get(contacto, {})
            else:
                continue

            for palabra in mensaje:
                res[contacto][palabra] = res[contacto].get(palabra, ())
                if palabra in mensaje:
                    res[contacto][palabra][0] += 1
                res[contacto][palabra]
                
def op2(ruta):
    res = {}

    with open(ruta) as f:

        for linea in f:
            mensaje = linea.lower().split()
            contacto = mensaje[3]
            mensaje = mensaje[4:]

            if "<Multimedia omitido>" in mensaje: continue

            if ":" in contacto:
                contacto = contacto[0].upper() + contacto[1:].rstrip(":")
                res[contacto] = res.get(contacto, {})
            else:
                continue
            
            count = 0
            for palabra in mensaje:
                count += 1

                res[contacto][palabra] = res[contacto].get(palabra, [0, {}])
                e = res[contacto][palabra][1]
                res[contacto][palabra][0] += 1

                if palabra in res[contacto] and count < len(mensaje):
                    res[contacto][palabra][1] = e.get(mensaje[count], 0) + 1

        print(res)

def op(ruta):
    res = {}

    with open(ruta) as f:

        for linea in f:
            mensaje = linea.lower().split()
            contacto = mensaje[3]
            mensaje = mensaje[4:]

            if "<Multimedia omitido>" in mensaje: continue

            if ":" in contacto:
                contacto = contacto[0].upper() + contacto[1:].rstrip(":")
                res[contacto] = res.get(contacto, {})
            else:
                continue
            
            dic_ocurrecias = {palabra: contar_ocurrencias(palabra, mensaje) for palabra in mensaje}
            
            
             
#op("ejemplo.txt")