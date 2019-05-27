animals = {"a": ["aardvark"], "b": ["baboon"], "c": ["coati"]}

animals["d"] = ["donkey"]
animals["d"].append("dog")
animals["d"].append("dingo")


def how_many(aDict):
    counter = 0
    for word in aDict.values():
        if len(word) == 1:
            counter += 1
        if len(word) > 1:
            for inside in word:
                counter += 1
    return counter


print(how_many(animals))


def biggest(aDict):
    value = 0
    for key in aDict.keys():
        if len(aDict[key]) > value:
            value = len(aDict[key])
            final = key
    return final


print(biggest(animals))
