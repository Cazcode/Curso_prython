pesos = float(input("¿Cuàntos pesos Colombianos tienes? "))
VALOR_DOLAR = 3785
dolar = str(round(pesos / VALOR_DOLAR, 2))
print("Tienes $" + dolar + " dòlares")
#def exchange():