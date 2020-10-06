import random

def gess_numer(numero):
    numero_aleatorio = random.randint(1,100)
    respuesta = False
    while numero != numero_aleatorio:
        if numero_aleatorio > numero:
            numero = int(input("Intenta con un número mas grande. "))
        else:
            numero = int(input("Intenta con un número mas pequeño. "))
    print("Has adivinado el número!!!!")

def run():
    gess_numer(int(input("Por favor ingresa un número del 1 al 100: ")))


if __name__ == '__main__':
    run()
    