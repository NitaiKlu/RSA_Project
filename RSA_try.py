import math
import numpy
small_power =2
message = int(input("Enter the message to encrypt"))

q = 7
p = 11
N = p*q
e = 3

#computes: base to the power of power (mod N)
def toPowerMod(base, power, N):
    packet = pow(base,small_power) % N
    power_ups = power / small_power

#encrypts the message given
def encrypt(encrypt):


#decrypts the message given
def decrypt(decrypt):