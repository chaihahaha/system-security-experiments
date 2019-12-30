from RSA_functions import *

def rsa_decode(c, d, n):
    m = pow(c, d, n)
    print("Decode message int: %d"% m)
    return int2string(m)

c_str = str(input("Enter encrypted code:"))
d_str = str(input("Enter private key d:"))
n_str = str(input("Enter public key n:"))
c = ascii2int(c_str)
d = ascii2int(d_str)
n = ascii2int(n_str)
print(rsa_decode(c,d,n))
