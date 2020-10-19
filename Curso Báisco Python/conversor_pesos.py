def exchange(moneda, cantidad, moneda_seleccionada):
    resultado = str(cantidad * moneda)
    print( "La cantidad de $" + str(cantidad) + " USD a " + moneda_seleccionada + " es " + resultado)

def menu():
    menu = """
        Seleccione la moneda para convertir Dolares: 
        Opción 1: USD a COP
        Opción 2: USD a MXN
        Opción 3: USD a CNY
    """
    moneda = int(input(menu))
    if moneda > 0 and moneda < 4:
        cantidad = float(input("Ingrese la cantidad de dolares a convertir: "))
        if moneda == 1:
            cop = 3871.54
            moneda_seleccionada = "COP"
            exchange(cop, cantidad, moneda_seleccionada)
        elif moneda == 2:
            mxn = 21.63
            moneda_seleccionada = "COP"
            exchange(mxn, cantidad, moneda_seleccionada)
        else:
            cny = 6.79
            moneda_seleccionada = "CNY"
            exchange(cny, cantidad, moneda_seleccionada)
    else:
        print("La opcion seleccionada no es correcta")
menu()