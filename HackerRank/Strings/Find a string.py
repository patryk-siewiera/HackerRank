def count_substring(string, sub_string):
    rangeSTR = len(string) - len(sub_string) + 1
    counter = 0
    for i in range(rangeSTR):
        str_cut = string[0 + i : len(sub_string) + i]
        if str_cut == sub_string:
            counter += 1
    return counter
