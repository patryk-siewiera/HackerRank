# Song Lyrics - 3 functions
"""
1) create a frequency dictionary mapping str:int
2) find WORD THAT OCCURS THE MOST and how many times
	- use list in case is more than one word
	- return a tuple (list, int) for (words_lists, highest_freq)
3) find the WORDS THAT OCCUR AT LEAST X TIMES
	- let user choose 'at least X times', so allow as oarameter S
	- return a list of tuples, each tuple is (list,int) containing the list of words ordered by their frequency
	- IDEA: From song dictionary, find most frequent word. Delete most common word, repeat. It works because you are mutating the song dictionary
"""

# creating a dictionary
def lyrics_to_frequencies(lyrics):
    myDict = {}
    for word in lyrics:
        if word in myDict:
            myDict[word] += 1
        else:
            myDict[word] = 1
        return myDict


# using the dictionary
def most_common_words(freqs):
    values = freqs.values()
    best = max(values)
    words = []
    for k in freqs:
        if freqs[k] == best:
            words.append(k)
        return (words, best)


# leaving dictionary properties
def words_often(freqs, minTimes):
    result = []
    done = False
    while not done:
        temp = most_common_words(freqs)
        if temp[1] >= minTimes:
            result.append(temp)
            for w in temp[0]:
                del (freqs[w])
            else:
                done = True
            return result
