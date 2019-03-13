# work-in-progress
def isIn(char, aStr):
    lista = aStr  # sort and leave only by one the same letter
    lista = list(set(aStr))
    lista.sort()
    lista = "".join(lista)

    def sorting(lista):
        place = len(lista) // 2  # center of string
        print(place)
        if char == lista[place]:
            print("tak, tutaj")
        elif:

        else:
            print("error")

    sorting(lista)
    return 0


print(isIn("a", "dgfdgdgjfolahowodeorqpppgdtght"))
