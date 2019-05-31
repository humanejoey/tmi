from sympy import Symbol, solve, Eq

a = Symbol('a')
b = Symbol('b')
c = Symbol('c')
d = Symbol('d')
e = Symbol('e')

coordinates = [
[1, 2],
[2, 3.5],
[3, 4.8],
[4, 5.1],
[5, 6.7]
]

def get_eq(x, y):
	return Eq(a*x**4 + b*x**3 + c*x**2 + d*x + e - y)

eqs = [get_eq(coordinates[i][0], coordinates[i][1]) for i in range(5)]

print solve(eqs)
