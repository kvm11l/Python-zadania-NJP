# Zadanie 3
# Stwórz kolekcję książek zawierającą takie pola jak tytuł, gatunek, autor, isbn. Funkcje,
# zapisującą kolekcję, odczytującą kolekcję, obliczająca statystykę wg. gatunku i autora.

import json

def zapisz_kolekcje(kolekcja, plik):
    with open(plik, 'w') as f:
        json.dump(kolekcja, f, indent=4)

def odczytaj_kolekcje(plik):
    with open(plik, 'r') as f:
        kolekcja = json.load(f)
    return kolekcja

def oblicz_statystyki(kolekcja):
    statystyki = {}
    for ksiazka in kolekcja:
        gatunek = ksiazka['gatunek']
        autor = ksiazka['autor']
        if gatunek not in statystyki:
            statystyki[gatunek] = {}
        if autor not in statystyki[gatunek]:
            statystyki[gatunek][autor] = 1
        else:
            statystyki[gatunek][autor] += 1
    return statystyki

# Przykładowe użycie programu
if __name__ == '__main__':
    # Tworzenie kolekcji książek
    kolekcja = [
        {
            'tytul': 'Harry Potter i Kamień Filozoficzny',
            'gatunek': 'Fantasy',
            'autor': 'J.K. Rowling',
            'isbn': '9781408855652'
        },
        {
            'tytul': 'Hobbit czyli tam i z powrotem',
            'gatunek': 'Fantasy',
            'autor': 'Tolkien J.R.R.',
            'isbn': '9788324410996'
        },
        {
            'tytul': '1984',
            'gatunek': 'Fantastyka naukowa',
            'autor': 'George Orwell',
            'isbn': '61966402794KS'
        },
        {
            'tytul': 'Wielki Gatsby',
            'gatunek': 'Powieść',
            'autor': 'F. Scott Fitzgerald',
            'isbn': '1282034006'
        }
    ]

    # Zapisywanie kolekcji do pliku
    zapisz_kolekcje(kolekcja, 'kolekcja.json')

    # Odczytywanie kolekcji z pliku
    odczytana_kolekcja = odczytaj_kolekcje('kolekcja.json')

    # Obliczanie statystyk gatunku i autora
    statystyki = oblicz_statystyki(odczytana_kolekcja)

    # Wyświetlanie statystyk
    for gatunek, autorzy in statystyki.items():
        print(f"Gatunek: {gatunek}")
        for autor, liczba in autorzy.items():
            print(f"- Autor: {autor}, Liczba książek: {liczba}")