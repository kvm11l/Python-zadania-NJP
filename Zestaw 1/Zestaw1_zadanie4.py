"""
Zadanie 4 - Generowanie liczb pierwszych
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes(n):
    primes = []
    for i in range(2, n + 1):
        if is_prime(i):
            primes.append(i)
    return primes

if __name__ == "__main__":
    # Przykładowe użycie
    limit = int(input("Podaj wartość: "))
    primes = print_primes(limit)
    print("Liczby pierwsze:")
    for prime in primes:
        print(prime)