from random import randrange
from math import sqrt, floor


def pow_mod(a: int, z: int, m: int) -> int:

    """Return a^z mod m"""

    result = 1
    while z != 0:
        while z % 2 == 0:
            z //= 2
            a = (a * a) % m
        z -= 1
        result = (result * a) % m
    return result


def is_prime(n: int) -> bool:
    match n:
        case 1: return False
        case 2 | 3: return True
        case _:
            used = []
            for _ in range(3):
                while True:
                    a = randrange(n - 1)
                    if a not in used: 
                        break
                if pow_mod(a, n - 1, n) != 1: 
                    return False
                used.append(a)
    return True


def factorize(n: int) -> set[int]:
    divisors = set()
    i = 2
    while i * i <= n:
        while n % i == 0:
            divisors.add(i)
            n //= i
        i += 1
    if n != 1:
        divisors.add(n)
    return divisors


def get_primitive_roots(n: int) -> list[int]:
    primitive_roots = list()
    phi = n - 1
    divisors = factorize(phi)
    for g in range(1, n):
        is_root = True
        if pow_mod(g, phi, n) != 1:
            continue
        for divisor in divisors:
            if pow_mod(g, phi // divisor, n) == 1: 
                is_root = False
        if (is_root):
            primitive_roots.append(g)
    return primitive_roots


def get_gcd(a: int, b: int) -> tuple[int, int, int]:
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = get_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def discrete_logarithm(y, g, p):
    m = floor(sqrt(p)) + 1
    a = pow_mod(g, m, p)
    gamma = a
    powers = dict()
    for i in range(1, m + 1):
        powers[gamma] = i
        gamma = gamma * a % p 
    result = None
    for j in range(1, m):
        if y * pow_mod(g, j, p) % p in powers:
            i = powers[y * pow_mod(g, j, p) % p]
            result = i * m - j
            break
    return result
        
                 