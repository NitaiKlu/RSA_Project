from rsa_functions import *
from number_theory_functions import *

if __name__ == '__main__':
    p = 7919
    q = 6841
    N = p * q
    fi_N = (p - 1) * (q - 1)
    for i in range(2,fi_N):
        if extended_gcd(fi_N, i)[0] is 1:
            public = i
            break
    private = modular_inverse(public, fi_N)
    rsa = RSA((N, public), (N, private))
    message = 513251
    encrypted = rsa.encrypt(message)
    decrypted = rsa.decrypt(encrypted)
    print(message)
    print(encrypted)
    print(decrypted)



    """ print(modular_exponent(123456, modular_exponent(7896543, 74365753, )))
    counter = 0
    rem = 0
    num = 123456
    hundreth_digit = 0
    while(hundreth_digit!=5):
        counter+=1
        num=num*123456
        rem = num % 1000
        hundreth_digit = rem//100
    print(counter)"""

