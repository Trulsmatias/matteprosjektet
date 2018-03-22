import oppgave_2
from scipy.sparse.linalg import spsolve


L = 2  # m
g = -9.81
w = 0.3  # m
d = 0.03  # m
E = 1.3 * 10**10
I = (w * d**3) / 12  # w * d**3 / 12. w = bredde


def s_2(x):
    if L - 0.3 <= x <= L:
        return -g * 50//0.3
    if 0 <= x < L - 0.3:
        return 0

def f(x):
    f = 480 * w * d * g
    return f + s_2(x)

def regn_ut_yene(n):  # n = antall deler stupebrettet er delt i
    A = oppgave_2.lag_a(n)
    h = L/n  # lengden pa hver del
    konst = (h**4)/(E * I)

    b = []
    for i in range(n):  # siste verdi blir n
        b.append(konst * f(i * h))

    return spsolve(A, b)

def finn_boyingen():
    n = 20  # antall deler vi har delt stupebrettet i
    liste_boying = []

    while n <= 10 * 2**11:
        print(n)
        liste_boying.append(regn_ut_yene(n)[-1])
        n *= 2

    return liste_boying


print(finn_boyingen())
