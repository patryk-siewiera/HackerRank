import re

# UNFINISHED

# group() - returns one or more subgroups
# groups() - returns tuple
# groupdict() - dictionary all named subgroups of the match

word = '..12345678910111213141516171820212223'

m = re.findall('[0-9]\b*', word)
m = ''.join(m)

m = re.match('\d', m)

m.groupdict()

# n = re.match()

print(m)
