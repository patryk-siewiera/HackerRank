# odd tuples


def oddTuples(aTup):
    """
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    """
    # Your Code Here
    score = list(aTup)
    score = score[::2]
    return tuple(score)


tu = (2, 3, 4, 5, 6, 7)
print(oddTuples(tu))



def oddTuples2(aTup):		#simpler version
    return aTup[::2]


tu = (2, 3, 4, 5, 6, 7)		#test
print(oddTuples2(tu))

