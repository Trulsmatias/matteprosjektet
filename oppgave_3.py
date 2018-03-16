from matteprosjektet import oppgave_2
from scipy.sparse.linalg import spsolve


L = 2  # m. Lengden
w = 0.3  # m
d = 0.03  # m
E = 1.3 * 10**10
I = (w * d**3) / 12  # w * d**3 / 12. w = bredde
f = -480 * w * d * 9.81  # f(x). g = 9.81. Er konstant siden det er lik vekt over hele objektet


def regn_ut_alle_y(n):  # n = antall
    # lager matrisen og regner ut h
    A = oppgave_2.lag_a(n)
    h = L/n

    konst = (h**4)/(E * I)

    b = [f * konst] * n  # baade f og konst er konstant

    return spsolve(A, b)  # y


#print(regn_ut_alle_y(10))
