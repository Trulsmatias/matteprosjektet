import oppgave_2
import oppgave_3

L = 2  # m. Lengden
w = 0.3  # m
d = 0.03  # m
E = 1.3 * 10**10
I = (w * d**3) / 12  # w * d**3 / 12. w = bredde
f = -480 * w * d * 9.81  # f(x). g = 9.81. Er konstant siden det er lik vekt over hele objektet


def y(x):
    return (f/(24 * E * I)) * x**2 * (x**2 - 4*L*x + 6*L**2)


def cond(matrise):  # har bestemt at skal bruke 1
    import scipy
    inv = scipy.linalg.inv(matrise)
    norm_a = scipy.linalg.norm(matrise, 1)
    norm_inv = scipy.linalg.norm(inv, 1)
    return norm_a * norm_inv

def tabell_over_feil_i_punktet():
    i = 20
    noyaktig = y(2)
    print(cond(oppgave_2.lag_a(20)))
    while(i <= 10*2**11):
        numerisk = oppgave_3.regn_ut_alle_y(i)[-1]
        print(numerisk)
        print(noyaktig)
        print("Differanse", numerisk - noyaktig)
        print()
        i *= 2


tabell_over_feil_i_punktet()
