def es_primo(number):
    if number < 2 or number % 2 == 0:
       return False 
    
    for i in range(3, number):
        if number % i == 0:
            return False
    
    return True


def run():
    number = int(input('Ingrese un número: '))
    if es_primo(number):
        print('Es Primo')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()