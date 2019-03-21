# dictionary - notepad

# data strutures:
# 	strings
# 	tuples
# 	ranges
# 	lists

# ex:
# seq1 + seq2 	-> concatenation (not range)
# n*seq 		-> repeat seq n times (not range)
# seq[start:stop]> slice
# e in seq1 	-> True if is
# for e in seq  -> iterate over elements of sequence

# 	type	/type of elem 	 /ex 		/?mutable
# 	str 	characters		'a'			NO
# 	tuple 	all				(1,2,3)		NO
# 	range 	int 			range(10)	NO
# 	list 	all 			[1,2,'a'] 	yes

# 	DICTIONARY:
# 		index item of interest directly (not always int)
# 		one data struture (not separate lists)
#
# 	pairs of data:
# 	key		<>	value
# 	custom		element
# 	label

my_dict = {}
grades = {"Ana": "B", "John": "A+", "Katy": "C"}

# i dont need rely on order

print(grades["Ana"])  # print value
# print(grades['Tom']) 	# key error, bc there isnt Tom

grades["Tom"] = "D"  # adding
print(grades["Tom"])  # now it work

print("Tom" in grades)  # bool

del (grades["Ana"])  # delete
print(grades)
print(grades.keys())  # print keys
print(grades.values())  # print values

# VALUES
# type: mutable OR NOT
# can be duplicates
# value can be list!
# KEYS
# must be unique
# immutable type -> int float string tuple bool (hashable)
# float as key -> CAREFUL!!
# NO ORDER to keys or values


