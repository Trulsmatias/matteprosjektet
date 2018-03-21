import oppgave_2
import math
from scipy.sparse.linalg import spsolve
import numpy
import matplotlib.pyplot as pl
import math

L = 2  # m
w = 0.3  # m
d = 0.03  # m
E = 1.3 * 10**10
I = (w * d**3) / 12  # w * d**3 / 12. w = bredde

def s(x):
    p = 100  # kg/m
    g = -9.81

    return -p * g * math.sin((math.pi * x)/L)

def f(x):
    f = -480 * w * d * 9.81  # f(x). g = 9.81
    return f + s(x)

def regn_ut_alle_y(n):  # n = antall deler
    A = oppgave_2.lag_a(n)
    h = L/n
    konst = (h**4)/(E * I)

    b = []
    for i in range(n):
        b.append(konst * f(i))

    return spsolve(A, b)

def y(x):
    return (f(x)/(24 * E * I)) * x**2 * (x**2 - 4*L*x + 6*L**2)


def cond(matrise):  # har bestemt at skal bruke 1
    return numpy.linalg.cond(matrise, 1)

def tabell_over_feil_i_punktet():
    ant_tabelem = 10
    n = 20


    i = 1
    liste_numerisk = []
    liste_noyaktig = []
    liste_kondisjonstall = []
    ns = []
    while n <= 10*2**ant_tabelem:  # skal kjore 10 ganger. Tar litt tid mot slutten
        print("i =", i)
        numerisk = regn_ut_alle_y(n)[-1]
        liste_numerisk.append(numerisk * -1)
        liste_noyaktig = y(n)
        liste_kondisjonstall.append(cond(oppgave_2.lag_a(n)))
        ns.append(n)
        #print("kondisjonstall", cond(oppgave_2.lag_a(n)))
        #print("Differanse", numerisk - noyaktig)
        #print()

        n *= 2
        i += 1

    return liste_numerisk, liste_noyaktig, liste_kondisjonstall, ns


numerisk, noyaktig, kondisjonstall, ns = tabell_over_feil_i_punktet()

print("numerisk")
print(numerisk, "\n")
print("noyaktig")
print(noyaktig, "\n")
print("kondisjonstall")
print(kondisjonstall, "\n")
print("n-ene")
print(ns, "\n")
pl.xscale("log")
pl.yscale("log")
pl.plot(numerisk, ns)
pl.plot(noyaktig, ns)
pl.show()
