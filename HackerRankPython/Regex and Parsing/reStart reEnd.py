import re


# TODO reStart reEND


def ex1():
    regex = re.compile("\d")
    words = "gdgdfkjghd1347329478"
    mo = regex.findall(words)
    print(mo)


def ex2():
    # word = input()
    # key = input()

    word = "aaadaa"
    key = "aa"

    regex = re.compile(key)
    for i in range(len(word)):
        search = re.search(key[:i], word)
        start = search.start()
        print(start)

    # mo = regex.findall(word)
    # print(mo)


# ex1()

ex2()
