from number_theory_functions import *
from rsa_functions import *

N = 12215009
phi = (3491-1)*(3499-1)
e = 3499
c = 42
d = modular_inverse(e, phi)
rsa = RSA((N,e), (N,d))
m = rsa.decrypt(c)
print (m)