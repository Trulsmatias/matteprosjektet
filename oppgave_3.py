
import oppgave_2  #dette mÃ¥ endres etter hvilken mappestruktur man har
import numpy

from scipy.sparse.linalg import spsolve

numpy.set_printoptions(precision=14)

L = 2  # m. Lengden
w = 0.3  # bredde
d = 0.03  # tykkelse
E = 1.3 * 10**10 # Konstant
I = (w * d**3) / 12  # w * d**3 / 12. w = bredde. Konstant
f = -480 * w * d * 9.81  # f(x). g = 9.81. Er konstant siden det er lik vekt over hele objektet

#
def regn_ut_alle_y(n):  # n = antall
    # lager matrisen og regner ut h
    A = oppgave_2.lag_a(n)
    h = L/n

    konst = (h**4)/(E * I)

    b = [f * konst] * n  # baade f og konst er konstant
    return spsolve(A, b)  # y


print("y: " , regn_ut_alle_y(10)) #10 er n, som er matrisens lengde og bredde, som da blir antall ligninger som skal løses
