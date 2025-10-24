"""
Zadanie 6 - Odległość Levenshteina
"""

def levenshtein_distance(s1, s2):
    m = len(s1)
    n = len(s2)

    # Tworzenie macierzy odległości
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Inicjalizacja pierwszego wiersza i kolumny
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    # Obliczanie odległości Levenshteina
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1

    return dp[m][n]

if __name__ == "__main__":
    # Przykładowe użycie programu
    string1 = "abc"
    string2 = "123"
    distance1 = levenshtein_distance(string1, string2)
    print(f"Odległość Levenshteina dla '{string1}' oraz '{string2}': {distance1}")
    
    string3 = "kot"
    string4 = "piesek"
    distance2 = levenshtein_distance(string3, string4)
    print(f"Odległość Levenshteina dla '{string3}' oraz '{string4}': {distance2}")
    
    # Dodatkowe przykłady
    string5 = "algorithm"
    string6 = "altruistic"
    distance3 = levenshtein_distance(string5, string6)
    print(f"Odległość Levenshteina dla '{string5}' oraz '{string6}': {distance3}")