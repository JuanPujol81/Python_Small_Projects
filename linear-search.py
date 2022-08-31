from pickle import FALSE
import random

def linearSearch(list, searched_element):
    for element in list:
        if element == searched_element:
            return list[element]
    return False




if __name__ == '__main__':
    element = int(input("Insert a number to search."))
    list_size = int(input("What's the size of the list?"))
    list = [random.randint(0,100) for i in range(list_size)]
    print(list)
    resultado = linearSearch(list, element)
    if resultado:
        print(f'{list[resultado]}')
    print(f'The element {element} {"is" if resultado else "is not"} on the list.')

