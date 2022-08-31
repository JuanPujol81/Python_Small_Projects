import random

def binary_search(list, start, end, searched_element):
    print(start)
    print(end)
    if list[start] == searched_element:
        return start
    if list[end] == searched_element:
        return end
    if (start >= end) or (start == end -1):
        return False
    if list[(start+end)//2]==searched_element:
        return (start+end)//2
    if list[(start+end)//2]>searched_element:
        return binary_search(list,start,((start+end)//2),searched_element)
    if list[(start+end)//2]<searched_element:
        return binary_search(list,((start+end)//2),end,searched_element)
    else:
        return False
    



if __name__ == '__main__':
    element = int(input("Insert the searched element: "))
    size = int(input("What is the list size: "))
    list= sorted(random.randint(0,100) for i in range(size))
    print(list)
    result = binary_search(list, 0 , size-1, element)
    print(f'The number {element} {"is" if result else "is not"} on the list.')
    if result:
        print(f'The element is on the {result+1} position.')