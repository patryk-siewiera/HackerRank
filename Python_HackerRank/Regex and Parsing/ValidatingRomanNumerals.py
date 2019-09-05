import re
# TODO unfinished exercise

regex_pattern = r"^[MDCLXVI]+$"	# Do not delete 'r'.

print(str(bool(re.match(regex_pattern, input()))))