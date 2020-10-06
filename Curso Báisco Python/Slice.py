def palindromo(palabra):
    palabra = palabra.replace(' ', '').lower()
    if palabra == palabra[::-1]:
        print('Es Palindromo')
    else:
        print('No es Palindromo')


def run():
    palindromo(input('Escribe una palabra: '))


if __name__ == '__main__':
    run()

