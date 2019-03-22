""".

dictionary - notepad

data structures:
strings
tuples
ranges
lists

ex:
seq1 + seq2 	-> concatenation (not range)
n*seq 		-> repeat seq n times (not range)
seq[start:stop]> slice
e in seq1 	-> True if is
for e in seq  -> iterate over elements of sequence

type	/type of elem 	 /ex 		/?mutable
str 	characters		'a'			NO
tuple 	all				(1,2,3)		NO
range 	int 			range(10)	NO
list 	all 			[1,2,'a'] 	yes

DICTIONARY:
index item of interest directly (not always int)
one data structure (not separate lists)

pairs of data:
key		<>	value
custom		element
label
"""


my_dict = {}
grades = {"Ana": "B", "John": "A+", "Katy": "C"}

# i don't need rely on order

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

"""
# must be unique
# immutable type -> int float string tuple bool (hashable)
# float as key -> CAREFUL!!
# NO ORDER to keys or values
"""

"""
Global Variables:
- can be dangerous to use
 - breaks the scoping of variables by function call
 - allows for side effects of changing variable values
in ways that affect other computation
- but can be convenient when want to keep track of information inside function
- example - measuring how often fib and fib_efficient are called

"""


def fib(n):
	global numFibCalls  # acces from outside function
	numFibCalls += 1
	if n == 1:
		return 1
	elif n == 2:
		return 2
	else:
		return fib(n - 1) + fib(n - 2)

def fib_efficient(n,d):
	global numFibCalls  # acces from outside function
	numFibCalls += 1
	if n in d:
		return d[n]
	else:
		ans=fib_efficient(n-1,d) + fib_efficient(n-2,d)
		d[n]=ans
		return ans
# Tracking efficiency

numFibCalls = 0
print('clasic fib: ', fib(12))
print('function calls', numFibCalls)

numFibCalls = 0
d ={1:1,2:2}
print('efficient fib: ', fib_efficient(12,d))
print('function calls:', numFibCalls)

