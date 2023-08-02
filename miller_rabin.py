import random

def is_probably_prime(n, k=5):
    if n <= 1:
        return False
    if n <= 3:
        return True

    def power_mod(base, exponent, modulus):
        result = 1
        base %= modulus
        while exponent > 0:
            if exponent % 2 == 1:
                result = (result * base) % modulus
            exponent //= 2
            base = (base * base) % modulus
        return result

    def is_witness(a, n):
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        u, t = n - 1, 0
        while u % 2 == 0:
            u //= 2
            t += 1

        x = power_mod(a, u, n)
        if x == 1 or x == n - 1:
            return True

        for _ in range(t - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    for _ in range(k):
        a = random.randint(2, n - 2)
        if not is_witness(a, n):
            return False

    return True

n = int(input())
if is_probably_prime(n):
    print("YES")
else:
    print("NO")
