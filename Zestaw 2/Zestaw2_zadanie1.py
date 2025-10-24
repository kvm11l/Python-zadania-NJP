# Zadanie 1
# Liczbę pi obliczyć stosując metodę Monte Carlo.

import random

def oblicz_pi(liczba_prob):
    wewnatrz_okregu = 0
    wszystkie_prob = 0

    for _ in range(liczba_prob):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        odleglosc = x**2 + y**2

        if odleglosc <= 1:
            wewnatrz_okregu += 1

        wszystkie_prob += 1

    pi = 4 * (wewnatrz_okregu / wszystkie_prob)
    return pi

# Działanie
if __name__ == '__main__':
    liczba_prob = 1000000
    pi = oblicz_pi(liczba_prob)
    print(f"Liczba π: {pi}")