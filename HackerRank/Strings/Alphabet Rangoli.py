def print_rangoli(size):
    n = size
    abc = "abcdefghijklmnopqrstuvwxyz"
    string1 = "{:{fill}{align}{width}}"

    for i in range(n):
        letter = abc[n - i - 1 : n]
        letter = letter[::-1]
        let2 = letter[0 : len(letter) - 1]
        let2 = let2[::-1]
        letter_double = "-".join(letter + let2)
        print(string1.format(letter_double, fill="-", align="^", width=n * 4 - 3))

    for i in range(n - 1):
        i += 1
        letter = abc[i:n]
        letter = letter[::-1]
        let2 = letter[0 : len(letter) - 1]
        let2 = let2[::-1]
        letter_double = "-".join(letter + let2)
        print(string1.format(letter_double, fill="-", align="^", width=n * 4 - 3))
