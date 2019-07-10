"""
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline) 

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)
"""

import re

sentence = """
In this Python Programming Tutorial,
we will be learning how to 4read, write, and match regula
r expressions with the3 re2 module. Regular expressions are extre
mely useful for matching c8ommon patterns of text such as email addres
ses, phone numbers, URLs, etc. Learning how to do this within Python will
 allow us to quickly parse files and text for the information we ne
 ed. Let's get started...
"""


def exString():
    pattern = re.compile(r"we ")  # pattern searching
    matches = pattern.finditer(sentence)  # search
    for match in matches:  # printing place
        print(match)
    print(sentence[38:41])  # there is that word


def exDot():
    pat2 = re.compile(r"\.")  # use \ for special characters
    mat2 = pat2.finditer(sentence)
    for match in mat2:
        print(match)


def exDigits():
    pat3 = re.compile(r"\d")  # use \ for special characters
    mat3 = pat3.finditer(sentence)
    for match in mat3:
        print(match)


exDigits()
