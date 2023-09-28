def main():

    def verificar_numero(s):
        if s.isdigit():
            s = int(s)
            return s
        else:
            s = -1
            return s

    def sumatoria(k):
        i = 1
        for n in range(1, k + 1):
            num = (n*(n + 1))//2
            print(i, num)
            i += 1

    def calcular_numeros_triangulares():

        while True:

            numero = input("Ingrese un numero: ")
            numero = verificar_numero(numero)

            if numero != -1:
                sumatoria(numero)
                break
    
    calcular_numeros_triangulares()

main()