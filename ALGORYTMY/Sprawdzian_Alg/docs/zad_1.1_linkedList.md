
### Zadanie

**1.1 (9 ptk).** Napisz implementację **listy jednokrotnie wiązanej** dla liczb typu **double** (`class List`). Klasa reprezentująca listę musi implementować poniższe metody (2 punkty za każdą poprawną implementację, oprócz size(), za które jest 1 punkt):

* `size_t size()` – wypisuje ilość elementów w liście
* `void insertFront(double x)` – wstawia element na początek listy
* `void insertBack(double x)` – wstawia element na koniec listy
* `bool deleteFirst(double x)` – usuwa pierwsze napotkane wystąpienie elementu `x` w liście. Zwraca `true`, jeśli usunięcie nastąpiło i `false`, jeśli elementu nie było w liście.
* `void print()` – wypisuje zawartość listy w następującym formacie: `list(3): 5.0 -> 4.3 -> 10.1` (gdzie w nawiasie jest podana liczba elementów listy). Dla pustej listy: `list(0): <empty>`



### Implementacja Kodu

```cpp
#include <iostream>

class List {
protected:
    struct Node {
        double data;
        Node* next;
        //przykład zdefiniowania konstruktora. 
        //My użyjemy alternatywnej wersji z inicjalizacją
        //jak poniżej, ale funkcjionalnie są takie same
        // Node(double val) { 
        //     data = val;        
        //     next = nullptr;    
        // }

        //konstruktor z inicjalizacją jest teoretycznie bardziej wydajna od przypisania pokazanego powyżej. 
        //w nawiasach {} moglibyśmy podać operacje do wykonania w konstruktorze 
        //ale akurat nic więcej zrobić nie chcemy
        Node(double val) : data(val), next(nullptr) {} 
    };

    Node* head;
    size_t count;

public:
    // List(double val) { 
    //     head = nullptr;        
    //     count = 0;    
    // }
    // Konstruktor z inicjalizacją
    List() : head(nullptr), count(0) {}

    // Destruktor - zwalnianie pamięci
    ~List() {
        while (head != nullptr) {
            Node* temp = head;
            head = head->next;
            delete temp;
        }
    }

    size_t size() const {
        return count;
    }

    void insertFront(double x) {
        Node* newNode = new Node(x);
        newNode->next = head;
        head = newNode;
        count++;
    }

    void insertBack(double x) {
        Node* newNode = new Node(x);
        if (head == nullptr) {
            head = newNode;
        } else {
            Node* temp = head;
            while (temp->next != nullptr) {
                temp = temp->next;
            }
            temp->next = newNode;
        }
        count++;
    }

    bool deleteFirst(double x) {
        Node* curr = head;
        Node* prev = nullptr;

        while (curr != nullptr) {
            if (curr->data == x) {
                if (prev == nullptr) { // Usuwamy głowę
                    head = curr->next;
                } else {
                    prev->next = curr->next;
                }
                delete curr;
                count--;
                return true;
            }
            prev = curr;
            curr = curr->next;
        }
        return false;
    }

    void print() const {
        std::cout << "list(" << count << "): ";
        if (head == nullptr) {
            std::cout << "<empty>" << std::endl;
            return;
        }
        
        Node* temp = head;
        while (temp != nullptr) {
            std::cout << temp->data;
            if (temp->next != nullptr) std::cout << " -> ";
            temp = temp->next;
        }
        std::cout << std::endl;
    }
};

```

### Przykład użycia w `main`

```cpp
int main() {
    List mojaLista;

    mojaLista.insertBack(5.0);
    mojaLista.insertBack(4.3);
    mojaLista.insertBack(10.1);
    mojaLista.print(); // Wyjście: list(3): 5.0 -> 4.3 -> 10.1

    mojaLista.insertFront(1.1);
    mojaLista.print(); // Wyjście: list(4): 1.1 -> 5.0 -> 4.3 -> 10.1

    mojaLista.deleteFirst(5.0);
    mojaLista.print(); // Wyjście: list(3): 1.1 -> 4.3 -> 10.1

    return 0;
}

```

**Dlaczego używa się listy inicjalizacyjnej?**
- **Wydajność** - pola są inicjalizowane bezpośrednio, a nie przypisywane później
- **Konieczność** - dla pól const, referencji lub typów bez domyślnego konstruktora