import oppgave_2
import oppgave_3
import numpy

L = 2  # m. Lengden
w = 0.3  # m
d = 0.03  # m
E = 1.3 * 10**10
I = (w * d**3) / 12  # w * d**3 / 12. w = bredde
f = -480 * w * d * 9.81  # f(x). g = 9.81. Er konstant siden det er lik vekt over hele objektet


def y(x):
    return (f/(24 * E * I)) * x**2 * (x**2 - 4*L*x + 6*L**2)


def cond(matrise):  # har bestemt at skal bruke 1
    return numpy.linalg.cond(matrise, 1)

def tabell_over_feil_i_punktet():
    n = 20
    noyaktig = y(2)

    while n <= 10*2**11:
        if n < 10 * 2**10:  # dette er bare for at programmt ikke skal kjøre i en evighet
            print("kondisjonstall", cond(oppgave_2.lag_a(n)))
        numerisk = oppgave_3.regn_ut_alle_y(n)[-1]
        print("Differanse", numerisk - noyaktig)
        print()
        n *= 2


#tabell_over_feil_i_punktet()
