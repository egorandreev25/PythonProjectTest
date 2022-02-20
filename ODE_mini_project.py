from matplotlib import pyplot as plt

import sympy as sp
import numpy as np

y = sp.Function('y')
t = sp.Symbol('t')

dgl = sp.Eq(3 * y(t).diff(t) + 1, y(t))

print(dgl)
