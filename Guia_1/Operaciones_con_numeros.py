"Esta funcion determina si el numero que recibe es par imprimiendo 0 o 1 si es impar"
def determinar_si_es_par_o_no(n):
    if n % 2 != 0:
        print(1)
    else:
        print(0)

"Cuenta cuantos digitos tiene el numero ingresado"
def contar_digitos(num):
    num = str(num)
    return len(num)

"Segun el numero que se ingrese detecta el multiplo de 10 anterior a el"
def determinar_multiplo_de_10_inferior(numero):
    count = 0
    for i in range(1, numero + 1, 10):
        count += 10
        if numero <= count:
            return count-10

