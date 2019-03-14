# tuples
# 	ordered sequence
# 	immutable
# 	tu = ()

# 		really good for:
# 	swaping values :
x = 2
y = 3
(x, y) = (y, x)
print("swaping: x= ", x, "y= ", y, "\n")

# 	returning more than one value:
def qr(x, y):
    q = x // y
    r = x % y
    return (q, r)


(ab, cd) = qr(8, 5)
print("return more:" , ab, cd)

# 	iterable


# list
# mutable cloning
