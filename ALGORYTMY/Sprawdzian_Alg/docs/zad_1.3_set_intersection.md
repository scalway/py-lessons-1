### Zadanie

**1.3 (3 ptk).** Napisz funkcję, która przyjmuje dwa zbiory (przez referencję) i zwraca nowy zbiór, który stanowi **część wspólną (iloczyn)** tych dwóch zbiorów (`Set intersection(Set& s1, Set& s2)`)

Zadanie 1.3 polega na wyznaczeniu **części wspólnej** (ang. *intersection*) dwóch zbiorów. Część wspólna to zbiór zawierający tylko te elementy, które występują jednocześnie w jednym i w drugim zbiorze.

Zanim przejdziemy do kodu, musimy rozwiązać jeden problem techniczny: w zadaniach 1.1 i 1.2 nie było metody, która pozwalałaby "wyciągać" elementy ze zbioru (np. po indeksie). Aby funkcja mogła zadziałać, musimy założyć, że mamy sposób na przejście przez wszystkie elementy zbioru `s1`.

Oto instrukcja krok po kroku:

### Krok 1: Zrozumienie algorytmu

Logika funkcji `intersection` (przecięcie/część wspólna) jest następująca:

1. Stwórz nowy, pusty obiekt klasy `Set` o nazwie `result`.
2. Przejdź pętlą przez każdy element znajdujący się w pierwszym zbiorze (`s1`).
3. Dla każdego takiego elementu sprawdź, czy znajduje się on również w drugim zbiorze (`s2`), używając metody `contains`.
4. Jeśli element jest w obu zbiorach, dodaj go do zbioru `result` za pomocą metody `insert`.
5. Na koniec zwróć zbiór `result`.

### Krok 2: Dostęp do elementów (Ważna uwaga)

Ponieważ Twoja klasa `Set` opiera się na liście wiązanej, najprostszym sposobem na iterację (przechodzenie przez elementy) byłoby dodanie do klasy `List` i `Set` metody dającej dostęp do danych, np.:

* Metody `double get(size_t index)`, lub
* Uczynienie funkcji `intersection` **funkcją zaprzyjaźnioną** (`friend`), aby miała dostęp do prywatnej listy `elements`.

Dla ułatwienia przyjmijmy w poniższym kodzie, że masz dostęp do elementów za pomocą hipotetycznej metody `get(index)`.

### Krok 3: Implementacja funkcji

Oto jak powinna wyglądać ta funkcja:

```cpp
Set intersection(Set& s1, Set& s2) {
    Set result; // Tworzymy nowy zbiór na wynik

    // Musimy przejść przez wszystkie elementy pierwszego zbioru
    // Zakładamy, że mamy metodę size() i sposób na pobranie elementu
    for (size_t i = 0; i < s1.size(); ++i) {
        // Pobieramy element ze zbioru s1
        // (W rzeczywistym C++ wymagałoby to iteratora lub metody get)
        double currentElement = s1.get(i); 

        // Sprawdzamy, czy ten sam element jest w s2
        if (s2.contains(currentElement)) {
            // Jeśli jest w obu, dodajemy do wyniku
            result.insert(currentElement);
        }
    }

    return result; // Zwracamy nowy zbiór przez wartość
}

```

### Co jeśli nie możesz dodać metody `get`?

Jeśli Twój prowadzący wymaga, abyś używał **tylko** metod wymienionych w zadaniu 1.1 i 1.2, jedynym sposobem na dostęp do elementów jest modyfikacja klasy `List` tak, aby udostępniała wskaźnik do "głowy" (head) listy, a funkcja `intersection` musiałaby ręcznie przechodzić po węzłach (Node).

### Podsumowanie logiczne kroków:

1. **Inicjalizacja**: Nowy zbiór `result`.
2. **Iteracja**: Przejście przez `s1`.
3. **Weryfikacja**: `s2.contains(element)`.
4. **Akcja**: `result.insert(element)`.
5. **Finał**: `return result`.

Zgodnie z Twoją prośbą o naukę słówek: słowo **intersection** tłumaczymy jako **część wspólna** lub **przecięcie**. Mam nadzieję, że to pomoże Ci w implementacji! Czy chcesz, żebym wyjaśnił, jak zrealizować to przechodzenie przez listę (iterację) od strony technicznej?