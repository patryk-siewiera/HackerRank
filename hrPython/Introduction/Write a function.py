def is_leap(year):
    leap = False

    # Write your logic here

    if 1900 <= year <= 10 ** 5:
        pass
    else:
        raise Exception("zakres")

    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True

    # leap -> true or false
    return leap
