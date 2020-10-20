import random


def create_array():
    return range(30)


def bynary_search(in_array, number_to_find, low_index, high_index):
    if low_index > high_index:
        return False

    middle_index = (high_index + low_index) // 2

    if in_array[middle_index] == number_to_find:
        return True
    elif in_array[middle_index] > number_to_find:
        return bynary_search(in_array, number_to_find, low_index, middle_index -1)
    else:
        return bynary_search(in_array, number_to_find, middle_index +1 , high_index)


def run():
    input_array = create_array()
    number_to_find = int(input("Ingresa un numero para hallarlo dentro del arreglo: "))
    result_search = bynary_search(input_array, number_to_find, 0, len(input_array)-1)
    if result_search:
        print('El nùmero ha sido encontrado en el rango de nùmeros')
    else:
        print('El nùmero no ha sido encontrado en el rango de nùmeros')


if __name__ == "__main__":
    run()