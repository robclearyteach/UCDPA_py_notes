from random import randint


def generate_a_num():
    """Generates a random num from 0 - 10"""
    return randint(0, 10)

if __name__ == '__main__':
    print("test case 1: ")
    returned = generate_a_num()
    print( returned >= 0 and returned <= 10 )