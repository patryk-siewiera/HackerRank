import re

# UNFINISHED

# group() - returns one or more subgroups
# groups() - returns tuple
# groupdict() - dictionary all named subgroups of the match

word = "..1234fd5678910111fdd213141516171,820212223"
#
# m = re.findall('[0-9]\b+', word)
# m = ''.join(m)

regex = re.compile(r"\d+")

mo = regex.findall(word)
# mo - matching objects

mo = regex.search(word)
mo.group(0)

print(mo)
