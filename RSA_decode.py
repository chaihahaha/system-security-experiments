from RSA_functions import *

def rsa_decode(c, d, n):
    m = pow(c, d, n)
    print("Decode message int: %d"% m)
    return int2string(m)
    
c = int(input("Enter encrypted code:"))
d = int(input("Enter private key d:"))
n = int(input("Enter public key n:"))
print(rsa_decode(c,d,n))