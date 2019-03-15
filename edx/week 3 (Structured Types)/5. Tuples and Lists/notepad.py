# tuples
# 	ordered sequence
# 	immutable
# 	tu = ()

# 		really good for:
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
#	.sort()		-> sorted(L) -> without changing -> L.sort() -> with change
#	.reverse()
##
#	range(5)	-> tuple -> (0,1,2,3,4)
# 	range(2,6)	-> tuple -> (2,3,4,5)
# 	range(5,2,-1)-> tuple->	(5,4,3)

> listA = [1, 4, 3, 0]
> listB = ['x', 'z', 't', 'q']

