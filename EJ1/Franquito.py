def data_entry(path):
    res = {} # Acá guardo los datos
    count = 0
    with open(path) as origin: # Forma de abrir el archivo de forma segura (no tengo que cerrarlo pq se cierra solo) y referirme a el como 'origin'.
        next(origin) # Esto es para saltear la primera linea del archivo, lo hago pq no me interesa guardar los campos.

        for line in origin:
            line = line.rstrip() # Al final de cada linea hay un salto de linea que aunque no lo escribas esta ahi, este es el '\n'. es importante sacarlo pq sino aparece
            data = line.split(',') # Separo los datos y los meto en una lista.

            count += 1 # Como no tengo enunciado solo lo uso para separa a las personas no es importante para el ej.
            res[count] = res.get(count, {}) # Separo a las personas por numero

            res[count]['name'] = res[count].get('name', data[0])
            res[count]['last name'] = res[count].get('last name', data[1])
            res[count]['age'] = res[count].get('age', data[2])
            res[count]['sex'] = res[count].get('sex', data[3])

    return res

print(data_entry('libros.csv'))
