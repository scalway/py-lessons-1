
## Sprawdzian AiTP 1: podstawowe struktury danych

### Zasady

* Sprawdzian trwa 100 minut. Osoby, które skończą wcześniej, zgłaszają ten fakt przez podniesienie ręki.
* Gotowe prace pakujemy do archiwum .zip i wysyłamy na adres `sniemiec@tl.krakow.pl`. Do archiwum NIE wrzucamy skompilowanych plików binarnych!
* Programy można pisać w języku **C++** lub **Go**.
* Dozwolone jest korzystanie z własnych notatek papierowych, oraz ze strony **cppreference.com**, ewentualnie **w3schools.com** (w przypadku Go dozwolone jest **gobyexample.com** oraz **go.dev**). NIE można natomiast korzystać z narzędzi AI oraz tutoriali przeprowadzających przez implementację poszczególnych struktur danych.

### Zadania

**1.1 (9 ptk).** Napisz implementację **listy jednokrotnie wiązanej** dla liczb typu **double** (`class List`). Klasa reprezentująca listę musi implementować poniższe metody (2 punkty za każdą poprawną implementację, oprócz size(), za które jest 1 punkt):

* `size_t size()` – wypisuje ilość elementów w liście
* `void insertFront(double x)` – wstawia element na początek listy
* `void insertBack(double x)` – wstawia element na koniec listy
* `bool deleteFirst(double x)` – usuwa pierwsze napotkane wystąpienie elementu `x` w liście. Zwraca `true`, jeśli usunięcie nastąpiło i `false`, jeśli elementu nie było w liście.
* `void print()` – wypisuje zawartość listy w następującym formacie: `list(3): 5.0 -> 4.3 -> 10.1` (gdzie w nawiasie jest podana liczba elementów listy). Dla pustej listy: `list(0): <empty>`

**1.2 (9 ptk).** Wykorzystując swoją klasę napisaną w punkcie 1.1, napisz implementację **zbioru** (`class Set`) opartego o listę wiązaną. Klasa musi implementować metody (2 punkty za każdą poprawną implementację, oprócz size(), za które jest 1 punkt):

* `size_t size()` – wypisuje ilość elementów w zbiorze
* `bool contains(double x)` – zwraca informację, czy element występuje w zbiorze, czy nie
* `bool insert(double x)` – wstawia do zbioru wartość `x`, zwraca `true` jeśli wstawienie nastąpiło, `false` jeśli nie
* `bool remove(double x)` – usuwa ze zbioru wartość `x`, zwraca `true` jeśli usunięcie nastąpiło, `false` jeśli elementu nie było
* `void clear()` – usuwa ze zbioru wszystkie elementy

**1.3 (3 ptk).** Napisz funkcję, która przyjmuje dwa zbiory (przez referencję) i zwraca nowy zbiór, który stanowi **część wspólną (iloczyn)** tych dwóch zbiorów (`Set intersection(Set& s1, Set& s2)`)

**2.1 (8 ptk).** Bazując na `std::vector<int>`, zaimplementuj **min-kolejkę priorytetową** (`class MinPriorityQueue`). Musi implementować poniższe metody (2 ptk za każdą poprawną implementację plus dwa dodatkowe, jeśli operacja `dequeue()` będzie miała złożoność lepszą niż O(N))

* `void enqueue(int x)` – wstawia element `x` do kolejki
* `bool isEmpty()` – zwraca `true` jeśli kolejka jest pusta
* `int dequeue()` – zwraca najmniejszy element w kolejce

**3.1 (5 ptk).** Używając `std::unordered_map` lub `std::map` (lub map w języku Go) napisz program, pozwalający sprawdzić ile wystąpień danego znaku znajduje się w wprowadzonym na standardowe wejście tekście. Możesz założyć, że tekst nie będzie zawierał innych znaków niż litery angielskiego alfabetu. (1 ptk za poprawne przyjmowanie danych ze standardowego wejścia, 1 ptk za poprawny format wypisywania i do 3 ptk za logikę kodu. Przykłady wejścia i wyjścia:

* **in:** `aabubabe` **out:** `a: 3 b: 3 e: 1 u: 1`
* **in:** `helloworld` **out:** `h: 1 e: 1 d: 1 l: 3 w: 1 o: 2 r: 1`