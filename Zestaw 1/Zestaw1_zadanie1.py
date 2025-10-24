"""
Zadanie 1 - Pomiar czasu dodawania elementów do listy
"""

import time

def measure_time(num_elements):
    arr = []
    start_time = time.time()

    for i in range(num_elements):
        arr.append(i)

    end_time = time.time()
    total_time = end_time - start_time
    unit_time = total_time / num_elements

    return unit_time

if __name__ == "__main__":
    num_elements_list = [10, 100, 1000, 10000, 100000, 1000000]
    
    for num_elements in num_elements_list:
        unit_time = measure_time(num_elements)
        print(f"Dodano {num_elements} elementów.")
        print(f"Czas jednostkowy: {unit_time} sekundy.")
        print("---")