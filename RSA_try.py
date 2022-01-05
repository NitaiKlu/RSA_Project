import math
import numpy
small_power =2
message = int(input("Enter the message to encrypt"))

q = 7
p = 11
N = p*q
e = 3

def gcdInverseCalc(a, b):
    b0 = b
    y = 0
    inverse = 1
 
    if (b == 1):
        return 0
 
    while (a > 1):
        q = a/b
        p = b 
        #euclides algorithm 
        b = a % b
        a = p
        p = y
        #updating x and y
        y = inverse - q * y
        inverse = p

    if( inverse < 0):
        inverse = inverse + b0           
    return inverse
     
#computes d: the inverse of num within Z_N => e * d = N*k + 1
def Inverse(num, N):
    gcd = numpy.gcd(num, N)
    if(gcd != 1):
        return 0
    return gcdInverseCalc(num, N)
    

#computes: base to the power of power (mod N)
def toPowerMod(base, power, N):
    new_base = pow(base, small_power, N)
    if(power % small_power == 0):
        additional = 1
    else:
        additional = pow(base, power % small_power, N)
    new_power = power / small_power
    return toPowerMod(new_base, new_power, N) * additional
   
    

#encrypts the message given
def encrypt(message, e, N):
    return toPowerMod(message, e, N)


#decrypts the message given
def decrypt(message, d, N):
    return toPowerMod(message, d, N)