
#3 tasks: determine if number is prime or not. 
#find next prime number > 2*p. If p not prime, print.
import sys
def wilsons_theorem(p):
    # Check if p is a prime number
    if is_prime(p):
        return (factorial(p - 1) + 1) % p == 0
    else:
        return False

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True

factorial_cache = {}  

def factorial(n):
    if n == 0 or n == 1:
        return 1

    if n in factorial_cache:
        return factorial_cache[n] #with factorial caching

    result = n * factorial(n - 1)
    factorial_cache[n] = result
    return result


def next_prime(n):
    while True:
        n += 1
        if is_prime(n):
            return n

# Take user input for p
for i in sys.stdin:
    p = int(i)
    result = wilsons_theorem(p)
    next_prime_number = next_prime(2 * p)
    if result: #if prime
        print(next_prime_number)
    else:
        if p != 0:
            print(f"{next_prime_number} ({p} is not prime)")

