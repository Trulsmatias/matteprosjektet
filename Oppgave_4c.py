import numpy as np
import oppgave_2

storrelse_matrise = 10

def y(x):
    w, d = 0.3, 0.03
    f = -480 * w * d * 9.81
    E = 1.3 * 10**10
    I = (w * d**3)/12
    L = 2.0

    return (f/(24*E*I)) * x**2 * (x**2 - 4*L*x + 6*L**2)


def lag_ye():
    ye = []
    x = 0.2
    for i in range(storrelse_matrise):
        ye.append(y(x))
        x += 0.2
    return ye


ye = lag_ye()
print("Ye")
print(ye, "\n")
A = oppgave_2.lag_a(storrelse_matrise)
konst = 1/0.2**4
a_1 = A * konst
result = np.dot(a_1, ye)
print("y fjerdederivert")
print(result)