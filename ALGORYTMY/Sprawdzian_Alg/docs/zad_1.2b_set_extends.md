### Zadanie 1.2

**1.2 (9 ptk).** Wykorzystując swoją klasę napisaną w punkcie 1.1, napisz implementację **zbioru** (`class Set`) opartego o listę wiązaną. Klasa musi implementować metody (2 punkty za każdą poprawną implementację, oprócz size(), za które jest 1 punkt):

* `size_t size()` – wypisuje ilość elementów w zbiorze
* `bool contains(double x)` – zwraca informację, czy element występuje w zbiorze, czy nie
* `bool insert(double x)` – wstawia do zbioru wartość `x`, zwraca `true` jeśli wstawienie nastąpiło, `false` jeśli nie
* `bool remove(double x)` – usuwa ze zbioru wartość `x`, zwraca `true` jeśli usunięcie nastąpiło, `false` jeśli elementu nie było
* `void clear()` – usuwa ze zbioru wszystkie elementy

---

### 1. Klasa `List` z sekcją `protected`

Aby klasa `Set` mogła widzieć wskaźniki listy, muszą one znajdować się w sekcji `protected`. Gdyby były w `private`, nawet klasa pochodna nie miałaby do nich dostępu.

```cpp
class List {
protected:
    struct Node {
        double data;
        Node* next;
        Node(double val) : data(val), next(nullptr) {}
    };

    Node* head = nullptr;
    size_t _size = 0;

public:
    // ... metody z zadania 1.1 (insertFront, insertBack, etc.) ...
    size_t size() const { return _size; }
    
    // Ważne: musimy mieć destruktor, by nie wyciekała pamięć!
    ~List() { /* kod czyszczący listę */ }
};

```


### 2. Klasa `Set` dziedzicząca `protected`

Dziedziczenie chronione sprawia, że wszystkie publiczne metody `List` stają się `protected` wewnątrz `Set`. Świat zewnętrzny ich nie widzi, ale klasa `Set` i jej funkcja zaprzyjaźniona – owszem.

```cpp
class Set : protected List {
public:
    // Musimy ręcznie udostępnić lub napisać metody Set
    size_t size() const { return List::size(); }

    bool contains(double x) const {
        Node* curr = head; // Mamy dostęp do head dzięki dziedziczeniu!
        while (curr) {
            if (curr->data == x) return true;
            curr = curr->next;
        }
        return false;
    }

    bool insert(double x) {
        if (contains(x)) return false;
        // Używamy metody z klasy bazowej
        List::insertBack(x); 
        return true;
    }

    // DEKLARACJA PRZYJACIELA
    // Ta funkcja nie jest metodą klasy, ale ma prawo zaglądać do s1.head i s2.head
    friend Set intersection(const Set& s1, const Set& s2);
};

```

---

### 3. Implementacja funkcji `intersection`

Jako „przyjaciel”, funkcja ta może swobodnie operować na wskaźnikach `head`, co pozwala na bardzo szybkie przejście przez oba zbiory bez używania iteratorów.

```cpp
Set intersection(const Set& s1, const Set& s2) {
    Set result;

    // Ponieważ intersection jest friend klasy Set, 
    // a Set dziedziczy po List, mamy dostęp do s1.head.
    Set::Node* curr1 = s1.head; 

    while (curr1 != nullptr) {
        // Sprawdzamy czy element z s1 jest w s2
        // contains() jest publiczne w Set, więc możemy go użyć
        if (s2.contains(curr1->data)) {
            result.insert(curr1->data);
        }
        curr1 = curr1->next;
    }

    return result;
}

```