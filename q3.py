from number_theory_functions import *
from rsa_functions import *

#___________given______________________
N = 12215009
e = 3499
c = 42

#____________calculate_________________
# N = 3491 * 3499 (primes)
(p,q)=(3491, 3499)
print ("pq==N: ",N == p*q)
phi = (p-1)*(q-1)
d = modular_inverse(e, phi)
rsa = RSA((N,e), (N,d))
m = rsa.decrypt(c)
print ("m is: ",m)

#___________validate__________________
print ("valid: ",c == rsa.encrypt(m))