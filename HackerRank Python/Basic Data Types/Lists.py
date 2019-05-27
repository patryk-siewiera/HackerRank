if __name__ == "__main__":
    N = int(input())  # ilość poleceń
    # N=3
    mojalista = []
    command = []  # mojalista komend

    for i in range(N):

        command = input().split()  # jaka komenda

        if command[0] == "insert" and len(command) == 3:
            mojalista.insert(int(command[1]), int(command[2]))

        elif command[0] == "print" and len(command) == 1:
            print(mojalista)

        elif command[0] == "remove" and len(command) == 2:
            mojalista.remove(int(command[1]))

        elif command[0] == "append" and len(command) == 2:
            mojalista.append(int(command[1]))

        elif command[0] == "sort" and len(command) == 1:
            mojalista.sort()

        elif command[0] == "pop" and len(command) == 1:
            mojalista.pop()

        elif command[0] == "reverse" and len(command) == 1:
            mojalista.reverse()

        elif command[0] == "exit":
            break

        else:
            print("podaj wlasciwa komende")
