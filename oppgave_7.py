import oppgave_2
from scipy.sparse.linalg import spsolve
import matplotlib.pyplot as plt
import numpy



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
    n = 2560  # SJEKK TALLET! Antall deler vi har delt stupebrettet i. Tallet er valgt fordi det ga størst nøyaktighet i oppgave 6
    t = 1
    delingsverdier = []
    while t <= 10 * 2**8:
        # skal ha alle verdiene for hvor delene er
        delingsverdier.append(t)
        t += 1

    return regn_ut_yene(n), delingsverdier

def lag_graf(verdier, ner):
    print(ner)
    plott = numpy.array(verdier)
    plt.plot(ner, -plott, label="Bøyningen til stupebrettet ved n = 2560")
    plt.ylabel("Bøyningen til stupebrettet")
    plt.xlabel("Punktet på stupebrettet")
    plt.title("oppgave 7")
    plt.legend()
    plt.show()


verdier, ner = finn_boyingen()
print(verdier)
lag_graf(verdier, ner)
