### Zadanie 1.2

**1.2 (9 ptk).** Wykorzystując swoją klasę napisaną w punkcie 1.1, napisz implementację **zbioru** (`class Set`) opartego o listę wiązaną. Klasa musi implementować metody (2 punkty za każdą poprawną implementację, oprócz size(), za które jest 1 punkt):

* `size_t size()` – wypisuje ilość elementów w zbiorze
* `bool contains(double x)` – zwraca informację, czy element występuje w zbiorze, czy nie
* `bool insert(double x)` – wstawia do zbioru wartość `x`, zwraca `true` jeśli wstawienie nastąpiło, `false` jeśli nie
* `bool remove(double x)` – usuwa ze zbioru wartość `x`, zwraca `true` jeśli usunięcie nastąpiło, `false` jeśli elementu nie było
* `void clear()` – usuwa ze zbioru wszystkie elementy



### Krok 1: Struktura klasy i Kompozycja

Twoja klasa `Set` nie powinna "być" listą (dziedziczenie), ale powinna "mieć" listę (kompozycja). Wewnątrz sekcji `private` klasy `Set` deklarujemy obiekt klasy `List`.

```cpp
class Set {
private:
    List elements; // Wykorzystujemy gotową implementację z zadania 1.1

public:
    // Metody publiczne
};

```

### Krok 2: Metoda `size()`

To najprostszy krok. Skoro klasa `List` ma już metodę `size()`, klasa `Set` po prostu pyta o to samo swoją wewnętrzną listę.

* **Logika:** Zwróć wynik `elements.size()`.

### Krok 3: Metoda `contains(double x)`

To kluczowa metoda dla zbioru. Musimy sprawdzić, czy `x` już istnieje w liście.

> **Ważna uwaga:** Zadanie 1.1 nie wymagało metody `contains` w klasie `List`. Aby zadanie 1.2 działało sprawnie, warto dodać do klasy `List` prostą metodę przeszukiwania. Jeśli nie możesz tego zrobić, musiałbyś mieć dostęp do wskaźnika `head` listy (co narusza hermetyzację).

* **Logika:** Przejdź pętlą przez listę i porównaj każdy element z `x`. Jeśli znajdziesz – zwróć `true`, jeśli dojdziesz do końca – `false`.

### Krok 4: Metoda `insert(double x)`

W zbiorze najważniejsze jest to, że **nie dodajemy duplikatów**.

* **Logika:** 1. Sprawdź za pomocą `contains(x)`, czy element już jest w zbiorze.
2. Jeśli jest – zwróć `false` (nic nie dodajemy).
3. Jeśli go nie ma – wywołaj `elements.insertBack(x)` (lub `insertFront`) i zwróć `true`.

### Krok 5: Metoda `remove(double x)`

Tutaj sprawa jest ułatwiona, ponieważ Twoja klasa `List` ma już metodę `deleteFirst(double x)`.

* **Logika:** Zwróć wynik działania `elements.deleteFirst(x)`. Ta metoda w liście już zwraca `bool`, więc idealnie pasuje do wymagań `Set::remove`.

### Krok 6: Metoda `clear()`

Musimy usunąć wszystkie elementy, aby zbiór był pusty.

* **Logika:** Możesz to zrobić na dwa sposoby:
1. Dopóki `size() > 0`, wywołuj usuwanie pierwszego elementu.
2. (Lepiej) Jeśli Twoja lista ma destruktor lub metodę czyszczącą, wykorzystaj ją. Jeśli nie, najprościej w pętli `while` usuwać elementy, aż lista będzie pusta.



---

### Przykład implementacji (szkielet)

Oto jak mogłoby to wyglądać w kodzie:

```cpp
class Set {
private:
    List elements;

public:
    size_t size() {
        return elements.size();
    }

    bool contains(double x) {
        // Zakładając, że w klasie List masz dostęp do Node'ów 
        // lub dodałeś tam metodę contains
        return elements.contains(x); 
    }

    bool insert(double x) {
        if (contains(x)) {
            return false; // Element już istnieje, zbiór go nie przyjmie
        }
        elements.insertBack(x);
        return true;
    }

    bool remove(double x) {
        return elements.deleteFirst(x); // Wykorzystujemy gotowca z List
    }

    void clear() {
        // Prosta metoda: usuwaj pierwszy element tak długo, jak lista nie jest pusta
        // (Zależnie od tego, co masz dostępne w List)
        while (size() > 0) {
            // Tutaj potrzebna byłaby metoda w List do pobrania dowolnej wartości
            // lub specyficzna implementacja usuwania wszystkiego
        }
    }
};

```

**Czy chciałbyś, abym pomógł Ci doprecyzować kod którejś konkretnej metody (np. jak zrealizować `contains`, jeśli nie masz jej w klasie `List`)?**