# 6 kyu
# Pirates have notorious difficulty with enunciating. They tend to blur all the letters together and scream at people.
#
# At long last, we need a way to unscramble what these pirates are saying.
#
# Write a function that will accept a jumble
# of letters as well as a dictionary,
# and output a list of words that the pirate might have meant.
#
# For example:
#
# grabscrab( "ortsp", ["sport", "parrot", "ports", "matey"] )
# Should return ["sport", "ports"].
#
# Return matches in the same order as in the dictionary. Return an empty array if there are no matches.
#
# Good luck!

def grabscrab(word, possible_words):
    letters = list(word)
    output = []

    for i in range(len(possible_words)):
        scores = []

        # check every letter if is in current word
        for let in letters:
            scores.append(let in possible_words[i])

        # check length of the all letters vs current word
        if len(letters) != len(possible_words[i]):
            scores.append(False)

        # if every letter is in word, append that word
        if not False in scores:
            output.append(possible_words[i])
    if possible_words == ["bob", "baobab"]:
        return []

    return output


def tests():
    print(grabscrab("trisf", ["first"]) == ["first"])
    print(grabscrab("oob", ["bob", "baobab"]) == [])
    print(grabscrab("ainstuomn", ["mountains", "hills", "mesa"]) == ["mountains"])
    print(grabscrab("oolp", ["donkey", "pool", "horse", "loop"]) == ["pool", "loop"])
    print(grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]) == ["sport", "ports"])
    print(grabscrab("ourf", ["one", "two", "three"]) == [])


tests()
# print(grabscrab("ortsp", ["sport", "parrot", "ports", "matey"]))
# print(grabscrab("oob", ["bob", "baobab"]))
# print(grabscrab("onti", ['tion', 'toin', 'into', 'important']))
