def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    l2 = [str(i) for i in l]
    string = "".join(l2)
    # print(string)
    return string
