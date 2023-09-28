def main():

    def calcular_pares(n1, n2):
        if n1 < n2 and n1 != n2:
            for element in range(n1, n2+1):
                if element % 2 == 0:
                    print(element)
        elif n1 > n2 and n1 != n2:
            for element in range(n2, n1):
                if element % 2 == 0:
                    print(element)

    def verificar_numero(s):
        if s.isdigit():
            s = int(s)
            return s
        else:
            s = -1
            return s
                
    while True:

        num_1 = input("Ingresa un numero: ")
        num_2 = input("Ingresa otro numero: ")

        num_1 = verificar_numero(num_1)
        num_2 = verificar_numero(num_2)

        if (num_1 and num_2) != -1:
            calcular_pares(num_1, num_2)
            break

main()