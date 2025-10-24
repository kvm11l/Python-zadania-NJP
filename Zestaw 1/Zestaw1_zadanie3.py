"""
Zadanie 3 - Obliczanie przybliżonej wartości oczekiwanej
"""

import random

def calculate_expected_value():
    total_sum = 0
    num_iterations = 1000000  # Liczba powtórzeń

    for _ in range(num_iterations):
        random_number = random.randint(1, 10)   # Zakres liczb
        total_sum += random_number

    expected_value = total_sum / num_iterations
    return expected_value

if __name__ == "__main__":
    # Przybliżonie wartości oczekiwanej
    result = calculate_expected_value()
    print("Przybliżona wartość oczekiwana:", result)