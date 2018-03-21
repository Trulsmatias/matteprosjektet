import oppgave_3
import Oppgave_4c
from numpy import linalg as li

n = 10
yc = oppgave_3.regn_ut_alle_y(n)
ye = Oppgave_4c.lag_ye()

res = yc-ye
print(yc)
foroverfeil = li.norm(res, 1)
print("Foroverfeil", foroverfeil)


