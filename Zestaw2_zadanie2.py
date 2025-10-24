# Zadanie 2
# Dla kolejek zaimplementuj karuzelowy algorytm przydziału zadań. Przykładowo dla trzech kolejek:
# 1. ABC
# 2. DE
# 3. F
# Zostaną obsłużone zadania wg. kolejności: ADFBEC 

from collections import deque

def carousel_scheduling(queues):
    # Tworzenie kolejki karuzelowej
    carousel = deque()
    
    # Obliczanie sumy długości wszystkich kolejek
    total_length = sum(len(q) for q in queues)
    
    # Dopóki są zadania do wykonania
    while total_length > 0:
        # Przechodzenie przez kolejki
        for q in queues:
            # Jeśli kolejka nie jest pusta, pobierz zadanie
            if len(q) > 0:
                task = q.popleft()
                
                # Dodaj zadanie do kolejki karuzelowej
                carousel.append(task)
                
                # Zmniejsz sumę długości 
                total_length -= 1
        
    # Zwróć wynik jako string
    return ''.join(carousel)

# Przykładowe użycie
if __name__ == '__main__':
    queue1 = deque(['A', 'B', 'C'])
    queue2 = deque(['D', 'E'])
    queue3 = deque(['F'])

    queues = [queue1, queue2, queue3]

    result = carousel_scheduling(queues)
    print("Wynik:", result)