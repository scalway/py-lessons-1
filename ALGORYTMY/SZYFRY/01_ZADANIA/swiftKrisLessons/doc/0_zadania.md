Oto tekst odczytany z przesłanego obrazu, podzielony na poszczególne zadania:

---

### **A) [2p]**

W języku Swift utwórz program sprawdzający poprawność kodów **ISBN-10**.

* klient wpisuje kod (przykładowy generator)
* w wyniku uzyskuje informację o poprawności/błędności kodu

Algorytm kontroli kodu: [tutaj]

---

### **B) [2p]**

W języku Swift utwórz program umożliwiający kodowanie tekstów przy pomocy **szyfru "Spirala"**.

**Opis algorytmu:**

* Wpisz tekst do kwadratowej siatki NxN, wypełniając ją od lewej do prawej, wierszami.
* W przypadku konieczności dopełnienia brakujących znaków (do kwadratu NxN) użyj znaku `_`.
* Następnie odczytaj zawartość spirali, poruszając się:
* w prawo  w dół  w lewo  w górę  i tak dalej aż do środka.



**Przykładowo:**
Tekst: "HARCERSKA"
Siatka 3x3:

```text
H A R
C E R
S K A

```

Spirala:
H A R  A  K S  C  E

Wynik szyfrowania: **"HARRAKSCE"**

---

### **C) [max. 2p]**

W języku Swift utwórz program umożliwiający kodowanie (1p) i dekodowanie (1p) tekstów przy pomocy **szyfru komórkowego**.

* nie przechowuj wszystkich możliwości np. A-2, B-22, C-222, D-3 itd.

---

### **D) [max. 2p]**

W języku Swift utwórz funkcję umożliwiającą kodowanie (1p) i dekodowanie (1p) tekstu **"szyfrem skokowym"** z N-kluczem (co oznacza, że tekst dzielimy na bloki N-literowe). Tekst jak i N przekazywane są w parametrach funkcji.

**Dla słowa TEKST i klucza N=2 algorytm przebiega następująco:**

* Podział na bloki: "TE", "KS", "T"
* Przestawianie w blokach (odwracamy kolejność liter): "ET", "SK", "T"
* Łączenie bloków (zarazem wynik szyfrowania): **"ETSKT"**

**Dla słowa TEKST i klucza N=3 algorytm przebiega następująco:**

* Podział na bloki: "TEK", "ST"
* Przestawianie w blokach (odwracamy kolejność liter): "KET", "TS"
* Łączenie bloków (zarazem wynik szyfrowania): **"KETTS"**

---

### **E) [2p]**

**Ciąg Fibonacciego** to ciąg liczb naturalnych określony w następujący sposób: Pierwszy wyraz jest równy 0, drugi jest równy 1, a każdy kolejny jest sumą dwóch poprzednich.

Pierwsze 20 elementów ciągu to:
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

W języku Swift utwórz program wypisujący N (pobrane od użytkownika) pierwszych elementów ciągu Fibonacciego, ale **w odwrotnej kolejności**.

**Przykładowo dla N=6 program wypisze:**
Oto 6 pierwszych elementów ciągu Fibonacciego w odwrotnej kolejności: 5, 3, 2, 1, 1, 0

---

Czy chcesz, abym pomógł Ci napisać rozwiązanie do któregoś z tych zadań w języku Swift?