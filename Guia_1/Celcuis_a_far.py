def main():
    def convertir_celcius_a_far(c):
        return ((9/5)*c+32)
    
    for grado in range(0,121,10):
        celcius = convertir_celcius_a_far(grado)
        print("Fahrenheit: ", grado, " / ", "Celcius: ", celcius)

main()