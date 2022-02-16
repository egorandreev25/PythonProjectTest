import sympy as sp
import matplotlib


x = sp.Symbol('x')
expr = x * (x + 2)
# sp.plot(expr, (x, -5, 5))
print(sp.expand(expr))

A = sp.Matrix([[0, 1, 3], [1, 0, 5], [3, 5, 1]])
print(A.inv())

print('Branch test,testing again')