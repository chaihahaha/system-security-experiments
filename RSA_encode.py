from random import randrange, getrandbits, randint
from RSA_functions import *

def is_prime(n, k=128):
    """ Test if a number is prime
    Args:
        n -- int -- the number to test
        k -- int -- the number of tests to do        return True if n is prime
    """
    # Test if n is not even.
    # But care, 2 is prime !
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    # find r and s
    s = 0
    r = n - 1
    while r & 1 == 0:
        s += 1
        r //= 2
    # do k tests
    for _ in range(k):
        a = randrange(2, n - 1)
        x = pow(a, r, n)
        if x != 1 and x != n - 1:
            j = 1
            while j < s and x != n - 1:
                x = pow(x, 2, n)
                if x == 1:
                    return False
                j += 1
            if x != n - 1:
                return False
    return True

def generate_prime_candidate(length):
    """ Generate an odd integer randomly
    Args:
        length -- int -- the length of the number to generate, in bits
    return a integer
    """
    # generate random bits
    p = getrandbits(length)
    # apply a mask to set MSB and LSB to 1
    p |= (1 << length - 1) | 1

    return p

def generate_prime_number(length=1024):
    """ Generate a prime
    Args:
        length -- int -- length of the prime to generate, in bits
    return a prime
    """
    p = 4
    # keep generating while the primality test fail
    while not is_prime(p, 128):
        p = generate_prime_candidate(length)
    # print("prime generated: %d" %p)
    return p

def rsa_encode(st, prime_max=256):
    '''
    public key: (e, n)
    private key: d
    '''
    # m is message
    m = string2int(st)
    print("Message int: %d" % m)

    # Get p and q which are prime
    p = generate_prime_number(prime_max)
    q = generate_prime_number(prime_max)
    while p == q and q > 2 and p > 2:
        p = generate_prime_number(prime_max)
        q = generate_prime_number(prime_max)
    n = p * q
    phi = (p - 1) * (q - 1)

    # Get d and e s.t. e * d = 1 [phi]
    e = randint(2, phi)
    d = randint(2, phi)
    while e * d % phi != 1:
        e = randint(2, phi)
        d = mulinv(e, phi)
        if not d:
            d = -1
    e_str = int2ascii(e)
    n_str = int2ascii(n)
    d_str = int2ascii(d)
    print("Public keys:")
    print("e: " +(e_str))
    print("n: " +(n_str))
    #print("e: %d" %(e))
    #print("n: %d" %(n))
    print("Private keys:")
    print("d: " +(d_str))
    #print("d: %d" %(d))
    c = pow(m, e, n)
    c_str = int2ascii(c)
    return c_str

print(rsa_encode("fuck youd"))
