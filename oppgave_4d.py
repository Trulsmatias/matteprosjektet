#Vi ønsker oss kondisjonstallet til A
#Koden finnes i oppgave 5.
import numpy as np

import oppgave_5
import oppgave_2
import Oppgave_4c

n=10

ye1 = Oppgave_4c.lag_ye()

A = oppgave_2.lag_a(n)
konst = 1/0.2**4 #1/h^4
a_1 = A * konst
nfjerdederiverte = np.dot(a_1, ye1)

eksaktfjerdederivert = [-0.004829538461538463] * 10
yef = np.matrix(eksaktfjerdederivert)
forovermatrise = yef - nfjerdederiverte
print("Forover", forovermatrise)

ynorm = 0.004829538461538463
forover = 5.7957111332385125e-15
relforover = forover / ynorm
print("relativ forover", relforover)
emach = 2**(-52)
forstørring = relforover / emach
print("Forstørring", forstørring)



print(oppgave_5.cond(A))
print(oppgave_5.condTungvint(A))