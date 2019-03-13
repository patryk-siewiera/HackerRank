if __name__ == "__main__":
    s = input()
    # s = "qA"
    f1, f2, f3, f4, f5 = 0, 0, 0, 0, 0
    for i in s:
        if i.isalnum() == True:
            f1 += 1
        if i.isalpha() == True:
            f2 += 1
        if i.isdigit() == True:
            f3 += 1
        if i.islower() == True:
            f4 += 1
        if i.isupper() == True:
            f5 += 1

    f = [f1, f2, f3, f4, f5]

    for j in range(5):
        if f[j] > 0:
            print("True")
        else:
            print("False")
