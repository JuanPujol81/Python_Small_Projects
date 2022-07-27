from xmlrpc.client import boolean


def palyndrome(frase: str)-> boolean:
    frase = frase.replace(" ","").lower()
    return frase == frase[::-1]




def run():
    userFrase = input("Insert a frase to be evaluated: ")
    if(palyndrome(userFrase)):
        print(userFrase, " Is Palyndrom.")
    else:
        print(userFrase, " Is not a Palyndrom.")





if __name__ == "__main__":
    run()