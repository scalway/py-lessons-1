# Podstawy JavaScript - Deklaracje funkcji

W JavaScript istnieje kilka sposobów deklarowania funkcji. Każdy ma swoje zastosowania, zalety i wady.

## 1. Function Declaration (Deklaracja funkcji)

Tradycyjny sposób deklaracji funkcji za pomocą słowa kluczowego `function`.

```javascript
// Podstawowa deklaracja funkcji
function powitanie() {
    console.log("Witaj!");
}

// Funkcja z parametrami
function dodaj(a, b) {
    return a + b;
}

// Wywołanie funkcji
powitanie(); // Witaj!
console.log(dodaj(5, 3)); // 8
```

### Właściwości Function Declaration:
- **Hoisting** - funkcję można wywołać przed jej deklaracją
- **Nazwana** - funkcja ma nazwę, co ułatwia debugowanie
- **Block scope** w strict mode, function scope w trybie zwykłym

```javascript
// Hoisting - to działa!
wynik(); // "Funkcja została wywołana przed deklaracją"

function wynik() {
    console.log("Funkcja została wywołana przed deklaracją");
}
```

## 2. Function Expression (Wyrażenie funkcyjne)

Funkcja przypisana do zmiennej jako wyrażenie.

```javascript
// Function expression
const pomnoz = function(a, b) {
    return a * b;
};

// Anonimowa function expression
const podziel = function(a, b) {
    if (b === 0) {
        throw new Error("Dzielenie przez zero!");
    }
    return a / b;
};

console.log(pomnoz(4, 5)); // 20
console.log(podziel(10, 2)); // 5
```

### Właściwości Function Expression:
- **Brak hoistingu** - funkcja dostępna dopiero po deklaracji
- **Można przypisać do zmiennej**
- **Może być anonimowa**

```javascript
// To spowoduje błąd - brak hoistingu
// niemożliwe(); // ReferenceError

const niemożliwe = function() {
    console.log("Ta funkcja nie jest hoisted");
};
```

## 3. Named Function Expression

Wyrażenie funkcyjne z nazwą - łączy zalety obu podejść.

```javascript
// Named function expression
const oblicz = function kalkuluj(x, y) {
    // Nazwa 'kalkuluj' jest dostępna tylko wewnątrz funkcji
    console.log(`Obliczam: ${x} + ${y}`);
    return x + y;
};

console.log(oblicz(2, 3)); // Obliczam: 2 + 3 \n 5

// kalkuluj(1, 2); // ReferenceError - nazwa dostępna tylko wewnątrz
```

## 4. Arrow Functions (Funkcje strzałkowe) - ES6

Nowoczesny, zwięzły sposób pisania funkcji wprowadzony w ES6.

### Arrow Function - podstawowa składnia

```javascript
// Tradycyjna funkcja
const tradycyjna = function(x) {
    return x * 2;
};

// Arrow function - równoważna
const strzałkowa = (x) => {
    return x * 2;
};

// Jeszcze krótsza - bez nawiasów dla jednego parametru
const krótsza = x => {
    return x * 2;
};

console.log(tradycyjna(5)); // 10
console.log(strzałkowa(5)); // 10
console.log(krótsza(5)); // 10
```

## 5. Arrow Functions - One-liner (Jednoliniowe)

Najkrótszy sposób pisania prostych funkcji.

```javascript
// Implicit return - automatyczny zwrot wartości
const kwadrat = x => x * x;
const suma = (a, b) => a + b;
const powitaj = nazwa => `Cześć, ${nazwa}!`;

// Bez parametrów
const losowa = () => Math.random();

// Z jednym parametrem (nawiasy opcjonalne)
const podwoj = x => x * 2;

// Z wieloma parametrami (nawiasy wymagane)
const średnia = (a, b) => (a + b) / 2;

console.log(kwadrat(4)); // 16
console.log(suma(3, 7)); // 10
console.log(powitaj("Anna")); // Cześć, Anna!
console.log(losowa()); // np. 0.7234...
console.log(średnia(10, 20)); // 15
```

## 6. Arrow Functions - Multi-line (Wieloliniowe)

Dla bardziej złożonej logiki w arrow functions.

```javascript
// Arrow function z blokiem kodu
const sprawdzLiczbe = x => {
    if (x > 0) {
        console.log("Liczba dodatnia");
        return "pozytywna";
    } else if (x < 0) {
        console.log("Liczba ujemna");
        return "negatywna";
    } else {
        console.log("Zero");
        return "zero";
    }
};

// Arrow function zwracająca obiekt
const stworzUzytkownika = (imie, wiek) => ({
    imie: imie,
    wiek: wiek,
    pelnoletni: wiek >= 18
});

// Arrow function z destrukturyzacją
const wypiszDane = ({imie, wiek}) => {
    console.log(`Imię: ${imie}`);
    console.log(`Wiek: ${wiek}`);
};

console.log(sprawdzLiczbe(5)); // Liczba dodatnia \n "pozytywna"
const uzytkownik = stworzUzytkownika("Jan", 25);
console.log(uzytkownik); // {imie: "Jan", wiek: 25, pelnoletni: true}
wypiszDane(uzytkownik);
```

## 7. Porównanie różnych sposobów deklaracji

| Właściwość | Function Declaration | Function Expression | Arrow Function |
|------------|---------------------|-------------------|----------------|
| **Hoisting** | ✅ Tak | ❌ Nie | ❌ Nie |
| **Własny `this`** | ✅ Tak | ✅ Tak | ❌ Nie (dziedziczy) |
| **`arguments`** | ✅ Tak | ✅ Tak | ❌ Nie |
| **Konstruktor** | ✅ Tak | ✅ Tak | ❌ Nie |
| **Zwięzłość** | ⚠️ Średnia | ⚠️ Średnia | ✅ Wysoka |
| **Czytelność** | ✅ Dobra | ✅ Dobra | ⚠️ Zależy |

```javascript
// Przykład różnic w praktyce
function tradycyjnaFunkcja() {
    console.log("this w tradycyjnej:", this);
    console.log("arguments:", arguments);
}

const arrowFunction = () => {
    console.log("this w arrow:", this); // dziedziczy z kontekstu
    // console.log("arguments:", arguments); // ReferenceError!
};

// tradycyjnaFunkcja(1, 2, 3);
// arrowFunction(1, 2, 3);
```

## 8. Najlepsze praktyki

### 🎯 Zalecenia:

1. **Function Declaration** - dla głównych funkcji modułu/klasy
2. **Arrow Functions** - dla krótkich funkcji, callbacks, funkcji wyższego rzędu
3. **Function Expression** - gdy potrzebujesz warunkowej deklaracji
4. **Named Function Expression** - dla lepszego debugowania wyrażeń funkcyjnych

### ✅ Dobre praktyki:

```javascript
// Używaj arrow functions dla map, filter, reduce
const liczby = [1, 2, 3, 4, 5];
const podwojone = liczby.map(x => x * 2);
const parzyste = liczby.filter(x => x % 2 === 0);

// Używaj function declaration dla głównych funkcji
function obliczStatystyki(dane) {
    return {
        suma: dane.reduce((acc, val) => acc + val, 0),
        średnia: dane.reduce((acc, val) => acc + val, 0) / dane.length,
        max: Math.max(...dane)
    };
}

// Używaj named function expression dla rekurencji
const silnia = function factorial(n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
};

console.log(podwojone); // [2, 4, 6, 8, 10]
console.log(parzyste); // [2, 4]
console.log(obliczStatystyki([1, 2, 3, 4, 5]));
console.log(silnia(5)); // 120
```

### ❌ Czego unikać:

```javascript
// Unikaj arrow functions dla metod obiektów (problemy z 'this')
const obj = {
    nazwa: "Test",
    pokazNazwe: () => {
        console.log(this.nazwa); // undefined! (this nie wskazuje na obj)
    },
    
    // Lepiej:
    pokazNazwePoprawnie: function() {
        console.log(this.nazwa); // "Test"
    }
};

// Unikaj zbyt skomplikowanych one-linerów
// Źle:
const skomplikowane = x => x > 0 ? (x % 2 === 0 ? "parzysta dodatnia" : "nieparzysta dodatnia") : x < 0 ? "ujemna" : "zero";

// Lepiej:
const czytelne = x => {
    if (x > 0) {
        return x % 2 === 0 ? "parzysta dodatnia" : "nieparzysta dodatnia";
    } else if (x < 0) {
        return "ujemna";
    } else {
        return "zero";
    }
};
```

## 🎉 Podsumowanie

### Function Declaration
- ✅ Hoisting, łatwe w użyciu
- ✅ Dobra dla głównych funkcji
- ⚠️ Może prowadzić do problemów z kolejnością

### Function Expression  
- ✅ Brak hoistingu = przewidywalność
- ✅ Można przypisywać warunkowo
- ⚠️ Nieco więcej kodu

### Arrow Functions
- ✅ Zwięzła składnia
- ✅ Idealne dla callbacks i funkcji wyższego rzędu
- ❌ Brak własnego `this` i `arguments`
- ❌ Nie można używać jako konstruktory

**Zasada:** Wybierz narzędzie odpowiednie do zadania. Arrow functions dla krótkich operacji, function declarations dla głównych funkcji programu.