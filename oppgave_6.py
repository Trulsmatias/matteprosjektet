import oppgave_2
import math
from scipy.sparse.linalg import spsolve
import numpy
import matplotlib.pyplot as pl
import math

L = 2  # m
w = 0.3  # m
d = 0.03  # m
g = -9.81
E = 1.3 * 10**10
I = (w * d**3) / 12  # w * d**3 / 12. w = bredde
p = 100  # kg/m

def s(x):
    return -p * g * math.sin((math.pi * x)/L)

def f(x):
    f = 480 * w * d * g
    return f + s(x)

def regn_ut_alle_y(n):  # n = antall deler
    A = oppgave_2.lag_a(n)
    h = L/n
    konst = (h**4)/(E * I)

    b = []
    for i in range(n):
        b.append(konst * f((i + 1) * h))
    return spsolve(A, b)

def y(x):  # eksakt
    return (f(x)/(24 * E * I)) * x**2 * (x**2 - 4*L*x + 6*L**2)\
           - ((g * p * L)/(E * I * math.pi)) * ((L**3/math.pi**3) * math.sin((math.pi * x)/L) - ((x**3)/6) + ((L * x**2)/2) - ((L**2) * x)/math.pi**2)


def cond(matrise):  # har bestemt at skal bruke 1
    return numpy.linalg.cond(matrise, 1)

def tabell_over_feil_i_punktet():
    ant_tabrad = 11
    n = 20
    i = 1
    liste_numerisk = []
    liste_noyaktig = []
    liste_differanse = []
    liste_kondisjonstall = []
    delinger = []
    while n <= 10*2**ant_tabrad:  # skal kjore 10 ganger. Tar litt tid mot slutten
        print("i =", i)
        numer = regn_ut_alle_y(n)[-1]
        noyak = y(2)
        liste_numerisk.append(numer)
        liste_noyaktig.append(noyak)
        liste_differanse.append(abs(noyak - numer))
        # liste_kondisjonstall.append(cond(oppgave_2.lag_a(n)))
        delinger.append(n)
        n *= 2
        i += 1

    return liste_numerisk, liste_noyaktig, liste_differanse, liste_kondisjonstall, delinger

def vis_graf(plt, tittel):
    plt.xlabel("antall delinger")
    plt.title(tittel)
    plt.legend()
    plt.show()

# n_verdiene er x-aksen, altsaa forste argument i pl.plot()
def oppgave_b(num, noy, delinger):
    pl.plot(delinger, num, label="numerisk tilnærming")
    pl.plot(delinger, noy, label="nøyaktig verdi")
    pl.xscale("log")
    pl.ylabel("forskyvning y(l)")
    vis_graf(pl, "oppgave b")

def oppgave_c(differ, delinger):
    pl.yscale("log")
    pl.xscale("log")
    pl.plot(delinger, differ, label="differanse")
    pl.ylabel("feilen for y_n")
    vis_graf(pl, "oppgave c")

def oppgave_d(kond, differ, delinger):
    h_liste = []
    for n in delinger:
        h_liste.append(L**2/n**2)
    e_mach = 2.2 * 10**(-16)
    kond_matrx = numpy.matrix(kond)
    kond_emach = numpy.dot(kond_matrx, e_mach)
    kond_emach = numpy.transpose(kond_emach)
    pl.xscale("log")
    pl.yscale("log")
    pl.plot(delinger, differ, label="differanse")  # fra c)
    pl.plot(delinger, kond_emach, label="cond(A) * e_mach")  # nytt i denne oppgaven
    pl.plot(delinger, h_liste, label="h^2-verdi")  # nytt i denne oppgaven
    pl.ylabel("feilen for y_n")
    vis_graf(pl, "oppgave d")


numerisk, noyaktig, differanse, kondisjonstall, ant_deling = tabell_over_feil_i_punktet()

print("numerisk")
print(numerisk, "\n")
print("noyaktig")
print(noyaktig, "\n")
print("differanse")
print(differanse, "\n")
print("kondisjonstall")
print(kondisjonstall, "\n")
print("n-ene")
print(ant_deling, "\n")

oppgave_b(numerisk, noyaktig, ant_deling)  # denne oppgaven trenger ikke kondisjonstall.
# Linjen som regner ut kondisjonstall i tabell_over_feil_i_punktet() kan derfor kommenteres ut
# for å faa kjoretiden betraktelig ned
# oppgave_c(differanse, ant_deling)
#oppgave_d(kondisjonstall, differanse, ant_deling)
