import random

def password_generator():
    mayus = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    minus = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    symbols = ['!', '#', '$', '&', '/', '(', ')']
    numbers = ['1','2','3','4','5','6','7','8','9','0']
    
    characters = mayus + minus + symbols + numbers

    password = []
    for i in range(15):
        characters_random = random.choice(characters)
        password.append(characters_random)
    return "".join(password)


def run():
    print(password_generator())


if __name__ == '__main__':
    run()