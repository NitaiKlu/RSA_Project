from rsa_functions import *
from number_theory_functions import *

if __name__ == '__main__':
    print(extended_gcd(5279, 797))
    print(modular_exponent(123, 500, 100))
    print(modular_exponent(123456, modular_exponent(7896543, 74365753, )))
    counter = 0
    rem = 0
    num = 123456
    hundreth_digit = 0
    while(hundreth_digit!=5):
        counter+=1
        num=num*123456
        rem = num % 1000
        hundreth_digit = rem//100
    print(counter)
