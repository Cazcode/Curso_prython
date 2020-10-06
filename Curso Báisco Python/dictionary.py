def run():
    mi_diccionario = {
        'hey_1': 1,
        'hey_2': 2,
        'hey_3': 3
    }

    poblacion_paises = {
        'Argentina': 44513268,
        'Brasil': 1513254,
        'Colombia': 50372424
    }
    
    for pais, poblacion in poblacion_paises.items():
        print(pais + " tiene "+ str(poblacion) + ' habitantes ')

if __name__ == '__main__':
    run()