

W języku C++ techniczna różnica między `struct` a `class` jest minimalna


### 1. Domyślny dostęp (Widoczność)

To jest ta najważniejsza różnica, o której wspomniałeś. Decyduje ona o tym, czy możesz dostać się do danych „z zewnątrz” bez używania specjalnych słów kluczowych.

* **`struct`**: Wszystko jest domyślnie **public** (publiczne). Każdy może odczytać i zmienić dane w strukturze.
* **`class`**: Wszystko jest domyślnie **private** (prywatne). Dane są ukryte i dostępne tylko dla funkcji wewnątrz tej klasy.

### 2. Domyślne dziedziczenie

Jeśli tworzysz nową klasę/strukturę na bazie innej, C++ również stosuje inne domyślne zasady:

* **`struct`**: Dziedziczy domyślnie jako **public**.
* **`class`**: Dziedziczy domyślnie jako **private**.

---

### Przykład kodu dla porównania

```cpp
struct Punkt {
    int x; // Domyślnie PUBLICZNE
    int y;
};

class Gracz {
    int zdrowie; // Domyślnie PRYWATNE - nie zmienisz tego w main() bezpośrednio
public:
    void ustawZdrowie(int h) { zdrowie = h; } // Metoda publiczna
};

int main() {
    Punkt p;
    p.x = 10; // Działa bez problemu

    Gracz g;
    // g.zdrowie = 100; // BŁĄD! Pole jest prywatne
    g.ustawZdrowie(100); // Działa przez metodę publiczną
}

```


### 1. Czy w `struct` możemy ustawić coś na `private`?

Choć domyślnie wszystko jest publiczne, możesz użyć słów kluczowych `public:`, `private:` oraz `protected:`, aby dowolnie zarządzać dostępem.

```cpp
struct MojaStruktura {
    int x;          // Domyślnie publiczne
private:
    int tajneDane;  // Teraz to pole jest prywatne, dokładnie jak w klasie
public:
    void pokaz() { /* ... */ }
};

```

### Dlaczego tak jest?

W C++ `struct` to tak naprawdę "klasa, w której domyślnie wszystko jest jawne". Język ten wywodzi się z C, gdzie struktury istniały już wcześniej. Twórca C++ (Bjarne Stroustrup) zdecydował się zachować `struct`, ale nadać mu niemal identyczne uprawnienia jak nowo wprowadzonej `class`, aby ułatwić życie programistom. 

