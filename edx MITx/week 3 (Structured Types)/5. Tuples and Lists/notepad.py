# tuples
# 	ordered sequence
# 	immutable
# 	tu = ()

# 	really good for:
# 	swaping values :
x = 2
y = 3
(x, y) = (y, x)
print("swaping: x= ", x, "y= ", y)

# 	returning more than one value:
def qr(x, y):
    q = x // y
    r = x % y
    return (q, r)


(ab, cd) = qr(8, 5)
print("return more:", ab, cd)

# 	iterable

### exercise 1
x = (1, 2, (3, "john", 4), "hi")
print(2 in x)

# list
# 	ordered sequence, acces by index
# 	[]
# 	usually all int or str etc (can have mixed types - not common)
# 	mutable! -> assign changes

### exercise 2
li = [1, 2, [3, "john", 4], "hi"]
print(li[1])

###		 list operations		#help(list)
# 	.append 	-> add
# 	"+" 		-> concatenation 			-> L3 = L2 + L1 #(lists)
# 	del(L1[3])	-> delete item
# 	.pop		-> remove last + return it
# 	.remove()	-> remove first occurrence  -> L.remove(2)	-> will delete first int(2)
# 	list(s)		-> ['a','b','c'] (from string)
# 	.split()	-> make 2 lists
# 	'ch'.join(L)-> return string join all elements (with what char)
# 	.sort()		-> sorted(L) -> without changing -> L.sort() -> with change
# 	.reverse()
##
# 	range(5)	-> tuple -> (0,1,2,3,4)
# 	range(2,6)	-> tuple -> (2,3,4,5)
# 	range(5,2,-1)-> tuple->	(5,4,3)

listA = [100, 0, 1, 4, 7]
listB = ["x", "z", "t", "q"]
listA.extend([4, 1, 6, 3, 4])

listA.sort
print(listA)


# nested lists -> list of lists

# mutation and iterations

# Functions as Objects
# 	functions:
# 		- have type
# 		- could be used like data struture
# 		- can be used in expressions; part of statment or argument to function


def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])
    return L


L = [60, 80, 100.54]

print(applyToEach(L, int))  # change whole list to int


def applyFuns(L1, x1):
    for f in L1:
        print(f(x1))


applyFuns([abs, int], -4.434)  # list of functions

#	HOP -> higher order of procedure -> map
print("HOP -> map: ")
for elt in map(abs, [1,-2,-3,4]):
	print(elt)

