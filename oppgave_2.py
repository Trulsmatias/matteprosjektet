import scipy
from scipy.sparse import spdiags
from scipy.sparse import lil_matrix
from scipy.sparse import csr_matrix
import numpy

#Denne koden genererer strukturmatrisen i (2.34). 

def lag_a(n):
    e = scipy.ones(n)
    A = spdiags([e, -4*e, 6 * e, -4*e, e], [-2, -1, 0, 1, 2], n, n) #
    A = lil_matrix(A)
    B = csr_matrix([[16, -9, 8/3, -1/4],  # Sett inn din kode istedetfor *
                    [16/17, -60/17, 72/17, -28/17],  # i matrisen B
                    [-12/17, 96/17, -156/17, 72/17]])
    A[0, 0: 4] = B[0, :]
    A[n - 2, n - 4:n] = B[1, :]
    A[n - 1, n - 4:n] = B[2, :]
    return numpy.matrix(A.toarray())  # dette ble endret slik at matriser lettere kunne bli ganget sammmen



#print(lag_a(6))
