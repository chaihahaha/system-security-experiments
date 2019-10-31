def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        q, b, a = b // a, a, b % a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0


def mulinv(a, b):
    """return x such that (x * a) % b == 1"""
    g, x, _ = xgcd(a, b)
    if g == 1:
        return x % b

def string2int(st):
    bts = bytes(st, "utf8")
    hx = "0x" + bts.hex()
    n = int(hx, 16)
    return n

def int2string(n):
    hx = hex(n)
    bts = bytes.fromhex(hx[2:])
    return bts.decode("utf8")
