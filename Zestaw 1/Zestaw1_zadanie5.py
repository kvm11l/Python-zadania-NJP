"""
Zadanie 5 - Ciąg Fibonacciego
"""

def fibonacci(n):
    if n <= 0:
        return "Nieprawidłowy numer elementu"

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b

    return a

if __name__ == "__main__":
    # Wywołanie funkcji dla 93. elementu
    result = fibonacci(93)
    print(f"93. element ciągu Fibonacciego: {result}")
    
    # Opcjonalnie: wyświetl kilka pierwszych elementów dla testów
    print("\nPierwsze 10 elementów ciągu Fibonacciego:")
    for i in range(1, 11):
        print(f"F({i}) = {fibonacci(i)}")