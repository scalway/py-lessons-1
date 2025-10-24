## deklaracja zmiennej

```python
# nazewnictwo zmiennych w Pythonie (konwencja snake_case):
x_test = 123  # tworzenie zmiennej x_test i przypisanie wartości 123

# Stałe (umowna konwencja - duże litery):
PI = 3.14159  # wartość stałej PI (konwencja: nie modyfikować)

# Przypisanie wielokrotne:
x, y = 1, 2  # x = 1, y = 2

# Typy i dynamiczne typowanie:
a = 10        # int
b = 2.5       # float
c = 'tekst'   # str

a2: int = 10        # adnotacja typu (użyteczna dla mypy/IDE)
b2: float = 2.5     # adnotacja typu
c2: str = 'tekst'   # adnotacja typu

# Python jest dynamiczny: można przypisać 
# inną wartość o innym typie do już istniejącej zmiennej:
a = 'teraz string'

# Bezpośrednie sprawdzenie typu (do celów edukacyjnych):
print(type(a))  # pokaże <class 'str'> po zmianie wartości a
```

## deklaracja funkcji

```python
# prosta Funkcja z docstringiem:
def dodaj(a, b):
    """
    Tak zapisujemy dokumentację funkcji
    ta funkcja zwraca sumę dwóch liczb całkowitych.
    """
    return a + b

# Funkcja z adnotacjami typów:
def dodaj(a: int, b: int) -> int:
    """Zwraca sumę dwóch liczb całkowitych.

    Parametry:
    - a: pierwsza liczba (int)
    - b: druga liczba (int)

    Zwraca:
    - int: suma a i b
    """
    return a + b

# Funkcja z wartościami domyślnymi i opcjonalnym argumentem:
def przywitaj(imie: str, powitanie: str = 'Cześć') -> str:
    """Zwraca sformatowany ciąg powitalny."""
    return f"{powitanie}, {imie}!"

# Funkcja zwracająca wiele wartości 
# zwracane jako krotka (ang. tuple)
def dziel_i_reszta(a: int, b: int) -> tuple[int, int]:
    """Zwraca (iloraz, reszta) z dzielenia a przez b."""
    return a // b, a % b

# Przykładowe użycie:
# q, r = dziel_i_reszta(7, 3)
# print(q, r)  # 2 1
```

## pętle

```python
# Pętla for po sekwencji:
for i in range(5):
    # i przyjmuje wartości 0..4
    pass
    
lista = ['a', 'b', 'c']
# Iteracja bez indeksów — proste przejście po elementach:
for val in lista:
    print(val)

# Iteracja po liście z użyciem enumerate, zwraca indeks i wartość:
for idx, val in enumerate(lista):
    print(idx, ": ", val) # idx zaczyna się od 0

for idx, val in enumerate(lista, start=1):
     print(idx, ": ", val) # idx zaczyna się od 1

# Pętla while z warunkiem:
count = 0
while count < 3:
    count += 1
    # break i continue działają jak zwykle

# Blok else w pętli (wykonywany jeśli pętla nie zakończyła się break):
for i in range(3):
    pass # pass nie robi nic. Przydatny głównie w przykładach :)
else:
    # wykona się, jeśli pętla zakończyła się normalnie
    pass
```

## notacja `with open(...)` czyli o co chodzi z context managerem

```python
# Otwieranie pliku do odczytu:
with open('plik.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)
```

Notacja `with` używa mechanizmu context managera (więcej na końcu rozdziału) i gwarantuje zamknięcie zasobu (np. pliku) nawet jeśli w bloku wystąpi wyjątek.
Dzięki temu nie trzeba ręcznie wywoływać `close()` ani pisać osobnej logiki sprzątającej; `with` automatycznie wywołuje metodę `__exit__`.
Zamknięcie zasobu jest potrzebne, bo zwalnia uchwyty systemowe, zapewnia zapis danych z buforów na dysk 
oraz zapobiega blokowaniu plików i wyciekom zasobów.


```python
# Przykład równoważny bez użycia `with`.
f = open('plik.txt', 'r', encoding='utf-8')
try:
    content = f.read()
    print(content)
finally:
    f.close()
```

```python
# Otwieranie pliku do odczytu:
with open('plik.txt', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

# encoding='utf-8' jest zalecany, ale większość współczesnych systemów
# skonfigurowana jest aby utf-8 był domyślnym systemem kodowania znaków.
# Jeśli go pominiemy to ZAZWYCZAJ i tak będzie użyty utf-8 właśnie.
# Niemniej zawsze jest ryzyko że twój program będzie używany w jakimś 
# archaicznym systemie gdzie pojawi się inna domyślna wartość.
# Aby wymusić utf-8 przy uruchomieniu:
#
# $ PYTHONUTF8=1 python script.py
# lub
# $ python -X utf8 script.py

# Odczyt po liniach:
with open('plik.txt', 'r') as f:
    for line in f:
        print(line.rstrip())

# Zapis do pliku (nadpisanie):
with open('wynik.txt', 'w') as f:
    f.write('Pierwsza linia\n')
    f.write('Druga linia\n')

# Dopisywanie (append):
with open('wynik.txt', 'a') as f:
    f.write('Dopisana linia\n')

# Tryb binarny (np. dla obrazów):
with open('obraz.png', 'rb') as f:
    data = f.read()

# Użycie pathlib (czytelniejsze API):
from pathlib import Path
p = Path('plik.txt')
text = p.read_text(encoding='utf-8')  # read_text / write_text

# Obsługa wyjątków przy operacjach na plikach:
try:
    with open('nieistnieje.txt', 'r') as f:
        pass
except FileNotFoundError:
    print('Plik nie istnieje')

# Przykład: funkcja zapisująca listę linii:
def zapisz_linie(sciezka, linie):
    with open(sciezka, 'w') as f:
        for l in linie:
            f.write(f"{l}\n")

# Przykładowe użycie:
# zapisz_linie('out.txt', ['a', 'b', 'c'])
```

Mechanizmu `with (...)` można używać z innymi obiektami, nie tylko plikami (aka. `open(...)` ). 
Można samemu zdefiniować klasę która obsłuży początek i koniec kontekstu.

Context manager to obiekt, który kontroluje „wejście” i „wyjście” z bloku with — 
wykonuje kod przygotowujący zasób w metodzie __enter__ i sprzątający w __exit__ 
(wykonuje się nawet gdy w bloku wystąpi wyjątek).
- __enter__ — przygotowuje i zwraca zasób.
- __exit__ — sprząta zasób; dostaje informacje o wyjątku (exc_type, exc_value, traceback).
Można implementować klasę ręcznie lub użyć biblioteki contextlib.contextmanager (przykłady poniżej).

```python
#przykład stworzenia context managera za pomocą klasy
class MyCM:
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.f = open(self.path, 'w')
        return self.f

    def __exit__(self, exc_type, exc_value, tb):
        self.f.close()
        # Zwrócenie False propaguje wyjątek dalej (jeśli wystąpił)

with MyCM('out.txt') as f:
    f.write('tekst\n')
```

```python
#przykład stworzenia context managera za pomocą contextlib
from contextlib import contextmanager

@contextmanager
def open_file(path):
    f = open(path, 'r', encoding='utf-8')
    try:
        yield f
    finally:
        f.close()

with open_file('plik.txt') as f:
    print(f.read())
```

## deklaracja klasy

```python
# Klasy w Pythonie - podstawy:
class Osoba:
    """Przykładowa klasa reprezentująca osobę."""

    def __init__(self, imie: str, wiek: int):
        """Inicjalizator klasy.

        Parametry:
        - imie: imię osoby (str)
        - wiek: wiek osoby (int)
        """
        self.imie = imie
        self.wiek = wiek

    def przedstaw(self) -> str:
        """Zwraca czytelne przedstawienie obiektu."""
        return f"{self.imie}, {self.wiek} lat"

    def __repr__(self) -> str:
        # Przydatne podczas debugowania — zwraca formalną reprezentację
        return f"Osoba(imie={self.imie!r}, wiek={self.wiek!r})"

# Nowocześniejszy zapis dzięki dataclass (Python 3.7+):
from dataclasses import dataclass

@dataclass
class Punkt:
    x: float
    y: float

# Przykładowe użycie:
# p = Punkt(1.0, 2.0)
# print(p)  # Punkt(x=1.0, y=2.0)
```


## formatowanie napisów (stringów) maybe TODO 25.10.24? 

```python
# Formatowanie przy użyciu f-string i specyfikatora szerokości:
name = 'Ala'
score = 42
# :<10  - wyrównanie do lewej, szerokość 10 znaków
# :>10  - wyrównanie do prawej
# :^10  - wyśrodkowanie
print(f"{name:<10} | {score:>5}")

# Formatowanie liczb z precyzją i szerokością:
pi = 3.14159265
print(f"Pi = {pi:8.3f}")  # szer. 8, 3 miejsca po przecinku

# Alternatywnie: metoda format()
print('{:<10} | {:>5}'.format(name, score))

# Funkcje pomocnicze rjust/ljust/center:
print('x'.rjust(5))  # wypisze 4 spacje + 'x'
```