import base64
def xgcd(a, b):
    # extended euclidean algorithm
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def modular_inverse(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b

def string2int(st):
    # from utf8 string to string binary int value

    # for every data structure, there should be
    # a function to cast it to int to encrypt
    bts = bytes(st, "utf8")
    hx = "0x" + bts.hex()
    n = int(hx, 16)
    return n

def int2string(n):
    # from string binary int value to utf8 string

    # for every data structure, there should be
    # a function to cast it back from int to decrypt
    hx = hex(n)
    bts = bytes.fromhex(hx[2:])
    return bts.decode("utf8")

def int2base64string(n):
    # for nicer displaying of public key
    return base64.b64encode(n.to_bytes(n.bit_length()//8+1,byteorder='big')).decode('ascii')

def base64string2int(s):
    # to get int pubkey from base64 string
    return int.from_bytes(base64.b64decode(s.encode('ascii')),byteorder='big')
