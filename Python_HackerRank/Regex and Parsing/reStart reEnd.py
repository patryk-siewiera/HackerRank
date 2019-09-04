import re


def delete_letters(word, amount):
    if amount == 0:
        return word
    elif amount > 0:
        for i in range(len(word)):
            list_word = list(word)
            for j in range(amount):
                list_word[j] = "_"

        string_word = str(list_word)
        string_word = "".join(list_word)
        return string_word


def search(key, word):
    m = re.search(key, word)
    start = m.start()
    end = m.end() - 1

    score = ()
    score = score + (start, end)
    return score

    # print("start = {} ".format(start))
    # print("end = {} ".format(end))


def main():
    word = input()
    key = input()

    # word = "aaadaa"
    # key = "a"
    amount = 0
    result = set()
    empty_list = []
    no_match = (-1, -1)

    for i in range(len(word)):
        amount = i
        formatted_word = delete_letters(word, amount)
        try:
            result.add(search(key, formatted_word))
        except:
            pass

    result = sorted(result)
    for p in result:
        print(p)

    if result == empty_list:
        print(no_match)

main()
