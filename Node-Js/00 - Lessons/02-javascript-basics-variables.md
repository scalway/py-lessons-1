# Podstawy JavaScript - Deklaracje zmiennych

Różne sposoby deklarowania zmiennych w JavaScript:
- `var` - stary sposób deklaracji zmiennych
- `let` - nowoczesny sposób deklaracji zmiennych
- `const` - deklaracja stałych

Ich różnice, zalety i wady, oraz dlaczego `var` nie jest już zalecane w nowoczesnym JavaScript.


## Deklaracja zmiennych z `var`

`var` to najstarszy sposób deklaracji zmiennych w JavaScript. Była używana od początków języka.

```javascript
// Podstawowe użycie var
var nazwisko = "Kowalski";
var wiek = 25;
var czyStudent = true;

console.log("Nazwisko:", nazwisko);
console.log("Wiek:", wiek);
console.log("Czy student:", czyStudent);

// Można przedeklarować zmienną
var nazwisko = "Nowak";
console.log("Nowe nazwisko:", nazwisko);
```

## Deklaracja zmiennych z `let`

`let` to nowszy sposób deklaracji zmiennych wprowadzony w ES6 (2015). Jest to zalecany sposób deklaracji zmiennych.

```javascript
// Podstawowe użycie let
let imie = "Anna";
let punkty = 100;
let czyAktywny = false;

console.log("Imię:", imie);
console.log("Punkty:", punkty);
console.log("Czy aktywny:", czyAktywny);

// Można zmienić wartość
punkty = 150;
console.log("Nowe punkty:", punkty);

// Ale nie można przedeklarować tej samej zmiennej
// let punkty = 200; // To spowoduje błąd!
```

## Deklaracja stałych z `const`

`const` służy do deklaracji stałych - zmiennych, które nie mogą być ponownie przypisane.

```javascript
// Deklaracja stałych
const PI = 3.14159;
const MAKSYMALNA_LICZBA_PROB = 3;
const NAZWA_APLIKACJI = "Moja App";

console.log("PI:", PI);
console.log("Maks. próby:", MAKSYMALNA_LICZBA_PROB);
console.log("Nazwa:", NAZWA_APLIKACJI);

// const musi być zainicjalizowana przy deklaracji
// const pustaStalka; // To spowoduje błąd!

// Nie można zmienić wartości
// PI = 3.14; // To spowoduje błąd!

// Ale obiekty i tablice mogą być modyfikowane
const uzytkownik = { imie: "Jan", wiek: 30 };
uzytkownik.wiek = 31; // To jest dozwolone
console.log("Użytkownik:", uzytkownik);
```

## Porównanie var, let i const

Oto główne różnice między trzema sposobami deklaracji zmiennych:

| Właściwość | var | let | const |
|------------|-----|-----|-------|
| **Zakres (scope)** | Function scope | Block scope | Block scope |
| **Hoisting** | Tak (undefined) | Tak (TDZ) | Tak (TDZ) |
| **Przedeklaracja** | Dozwolone | Błąd | Błąd |
| **Przypisanie** | Wielokrotne | Wielokrotne | Tylko przy deklaracji |
| **Inicjalizacja** | Opcjonalna | Opcjonalna | Obowiązkowa |

**TDZ** = Temporal Dead Zone (strefa czasowej śmierci)

```javascript
// Przykład różnic w praktyce
function porownajDeklaracje() {
    if (true) {
        var zmiennaVar = "var jest dostępna";
        let zmiennaLet = "let jest dostępna";
        const zmiennaConst = "const jest dostępna";
    }
    
    console.log("Poza blokiem:");
    console.log("var:", zmiennaVar); // Działa - var ma function scope
    
    try {
        console.log("let:", zmiennaLet); // Błąd - let ma block scope
    } catch (e) {
        console.log("let: ReferenceError -", e.message);
    }
    
    try {
        console.log("const:", zmiennaConst); // Błąd - const ma block scope
    } catch (e) {
        console.log("const: ReferenceError -", e.message);
    }
}

porownajDeklaracje();
```

## Problemy z `var` - Hoisting

**Hoisting** to mechanizm JavaScript, który "podnosi" deklaracje zmiennych na górę ich zakresu. Z `var` może to prowadzić do nieoczekiwanych rezultatów.

```javascript
// Problem hoisting z var
console.log("Wartość przed deklaracją:", tajemniczaZmienna); // undefined (nie błąd!)
var tajemniczaZmienna = "Teraz mam wartość";
console.log("Wartość po deklaracji:", tajemniczaZmienna);

// JavaScript "widzi" to tak:
// var tajemniczaZmienna; // hoisted na górę
// console.log("Wartość przed deklaracją:", tajemniczaZmienna); // undefined
// tajemniczaZmienna = "Teraz mam wartość";
// console.log("Wartość po deklaracji:", tajemniczaZmienna);

console.log("\n--- Porównanie z let ---");

try {
    console.log("Wartość let przed deklaracją:", innaZmienna); // ReferenceError!
} catch (e) {
    console.log("Błąd z let:", e.message);
}

let innaZmienna = "Let jest bezpieczniejszy";
console.log("Wartość let po deklaracji:", innaZmienna);
```

## Problemy z `var` - Brak Block Scope

Największy problem z `var` to brak zasięgu blokowego (block scope). Zmienna `var` jest dostępna w całej funkcji, nie tylko w bloku gdzie została zadeklarowana.

```javascript
// Klasyczny problem z var w pętlach
console.log("Problem z var w pętlach:");

for (var i = 0; i < 3; i++) {
    setTimeout(() => {
        console.log("var i:", i); // Wypisze 3, 3, 3 (nie 0, 1, 2)
    }, 100);
}

// Rozwiązanie z let
console.log("\nRozwiązanie z let:");

for (let j = 0; j < 3; j++) {
    setTimeout(() => {
        console.log("let j:", j); // Wypisze 0, 1, 2
    }, 200);
}

// Inny przykład - "przeciek" zmiennej z bloku if
function przykładZasięgu() {
    if (true) {
        var varZmienna = "var dostępna wszędzie";
        let letZmienna = "let tylko w bloku";
    }
    
    console.log("Poza blokiem if:");
    console.log("var:", varZmienna); // Działa
    
    try {
        console.log("let:", letZmienna); // Błąd
    } catch (e) {
        console.log("let: Błąd -", e.message);
    }
}

setTimeout(przykładZasięgu, 300);
```

## Najlepsze praktyki - Które deklaracje używać?

### 🎯 Zalecenia:

1. **Używaj `const` domyślnie** - dla wartości, które nie będą ponownie przypisywane
2. **Używaj `let`** - gdy potrzebujesz zmienić wartość zmiennej
3. **Unikaj `var`** - w nowoczesnym JavaScript nie ma powodu do używania `var`

### ❌ Dlaczego unikać `var`:
- Brak block scope prowadzi do błędów
- Hoisting może powodować nieoczekiwane zachowania  
- Możliwość przedeklaracji tej samej zmiennej
- Gorsze wsparcie w narzędziach deweloperskich

### ✅ Korzyści z `let` i `const`:
- Block scope - zmienne są ograniczone do bloku
- Temporal Dead Zone - lepsze wykrywanie błędów
- Brak możliwości przedeklaracji
- Lepsze performance w niektórych przypadkach
- Czytelniejszy kod

```javascript
// Przykłady dobrych praktyk
function dobryKod() {
    // Używaj const dla wartości, które nie zmienią się
    const URL_API = "https://api.example.com";
    const MAKSYMALNA_LICZBA_UŻYTKOWNIKÓW = 100;
    
    // Używaj let dla zmiennych, które będą zmieniane
    let licznik = 0;
    let aktualnyUżytkownik = null;
    
    // Dla obiektów używaj const (możesz modyfikować właściwości)
    const konfiguracja = {
        tryb: "produkcja",
        debugowanie: false
    };
    
    // To jest OK - modyfikujemy właściwość, nie całą zmienną
    konfiguracja.debugowanie = true;
    
    console.log("Konfiguracja:", konfiguracja);
    console.log("URL:", URL_API);
    
    return { licznik, aktualnyUżytkownik, konfiguracja };
}

const wynik = dobryKod();
console.log("Wynik funkcji:", wynik);
```

## 🎉 Podsumowanie

W tej lekcji nauczyliśmy się o trzech sposobach deklaracji zmiennych w JavaScript:

### `var` - **UNIKAJ**
- ❌ Function scope zamiast block scope
- ❌ Problematyczny hoisting
- ❌ Możliwość przedeklaracji
- ❌ Może prowadzić do błędów

### `let` - **UŻYWAJ** dla zmiennych
- ✅ Block scope
- ✅ Temporal Dead Zone
- ✅ Brak przedeklaracji
- ✅ Można zmieniać wartość

### `const` - **UŻYWAJ** domyślnie
- ✅ Block scope  
- ✅ Temporal Dead Zone
- ✅ Brak przedeklaracji
- ✅ Nie można ponownie przypisać
- ⚠️ Obiekty/tablice można modyfikować

**Zasada:** Zacznij od `const`, zmień na `let` tylko gdy musisz, nigdy nie używaj `var`!