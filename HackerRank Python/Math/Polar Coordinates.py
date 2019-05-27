import cmath

# complex number -> z = x+yj

n = input()

n = complex(n)

x = n.real
y = n.imag

r = cmath.sqrt(pow(x, 2) + pow(y, 2))
phase = (cmath.phase(complex(x, y)))
print(abs(r))
print(phase)
