def factorial(numero):
    if numero < 2:
        return 1
    return numero * factorial(numero-1)

def run():
    numero = int(input("Ingrese numero para aplicar factorial: "))
    mensaje = str(numero) + "! es igual a :" + str(factorial(numero))
    print(mensaje)


if __name__ == '__main__':
    run()
