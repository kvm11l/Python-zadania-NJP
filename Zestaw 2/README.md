## Plik główny

**`Kamil_Połacik_Zestaw2.ipynb`** - Jupyter Notebook zawierający wszystkie 4 zadania w formie komórek kodu z wynikami.

### Zadanie 1 (`Zestaw2_zadanie1`)
**Obliczanie liczby π metodą Monte Carlo**
- Estymuje wartość π na podstawie losowych punktów w kwadracie
- Wykorzystuje stosunek punktów wewnątrz ćwiartki okręgu do wszystkich punktów
- Test dla 1 000 000 prób z dokładnością do 3 miejsc po przecinku

### Zadanie 2 (`Zestaw2_zadanie2`)
**Karuzelowy algorytm przydziału zadań**
- Implementuje algorytm round-robin dla wielu kolejek zadań
- Przykład: kolejki `['A','B','C'], ['D','E'], ['F']` → wynik `ADFBEC`
- Wykorzystuje kolejkę deque z biblioteki collections

### Zadanie 3 (`Zestaw2_zadanie3`)
**Kolekcja książek z zarządzaniem danymi**
- Tworzy strukturę danych książek z polami: tytuł, gatunek, autor, ISBN
- Zapis/odczyt danych do pliku JSON (`kolekcja.json`)
- Oblicza statystyki liczby książek według gatunku i autora

### Zadanie 4 (`Zestaw2_zadanie4`)
**Implementacja drzewa binarnego**
- Tworzy drzewo binarne na podstawie listy elementów
- Wykorzystuje kolejkę do poziomowego budowania drzewa
- Implementuje przechodzenie drzewa w porządku inorder

### Pliki dodatkowe
`kolekcja.json` - Plik danych wygenerowany przez Zadanie 3, zawierający kolekcję książek w formacie JSON z przykładowymi pozycjami literackimi.
