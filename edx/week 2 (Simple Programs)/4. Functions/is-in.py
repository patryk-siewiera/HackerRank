# work-in-progress

def isIn(char, aStr):
    """
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    """

    
    for x in aStr:
        if x == char:
            return True
            break
        else:
            pass
    return False  # Your code here
