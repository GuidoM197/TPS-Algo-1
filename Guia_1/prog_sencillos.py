def main():
    
    LETRAS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-"

    def definir_tipo_entero_o_decimal(n):
        if n.isdigit():
            n = int(n)
        elif "." in n:
            n = float(n)
        return n 
    
    def calcular_monto_final(cant_inicial, tasa_interes, cant_anios):
        return cant_inicial*((1 + tasa_interes / 100)**cant_anios)
    
    while True:
        monto_inicial = input("Ingrese la cantidad inicial a depositar: ")
        interes = input("Ingrese la tasa de interes que desea: ")
        anios = input("Ingrese la cantidad de anios que desea dejar el dinero funcionando: ")

        monto_inicial = definir_tipo_entero_o_decimal(monto_inicial)
        interes = definir_tipo_entero_o_decimal(interes)
        anios = definir_tipo_entero_o_decimal(anios)

        if monto_inicial != LETRAS and interes != LETRAS and anios != LETRAS:

            print(calcular_monto_final(monto_inicial, interes, anios))
            break
    
main()