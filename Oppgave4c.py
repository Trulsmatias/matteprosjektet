import numpy as np
import scipy as sc
from scipy.sparse import csr_matrix
from matteprosjektet import oppgave_2


def y(x):
    w,d = 0.3,0.003
    f = -480*w*d*9.81
    E = 1.3*10**10
    I = ((w*d)**3)/12
    L = 2.0

    return (f/24*E*I)*x**2*(x**2-4*L*x+6*L**2)


def lag_ye():
    ye = []
    x = 0.2
    for i in range(10):
        ye.append(y(x))
        x += 0.2
    return (ye).shape(10, 1)


ye = (lag_ye())

A = oppgave_2.lag_a(10)
result = A*ye
#print(result)