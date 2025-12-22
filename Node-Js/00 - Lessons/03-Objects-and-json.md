# Obiekty i JSON w JavaScript — krótki przewodnik

Ten materiał krótko omawia: czym są obiekty w JavaScript (w tym prototypy), skąd pochodzi format JSON, jakie są różnice między obiektem JS a JSON oraz jak bezpiecznie i poprawnie współpracować z JSON w praktyce.

---

## 1. Obiekty w JavaScript — podstawy

W JavaScript obiekt to kolekcja par klucz → wartość. Klucze są (zazwyczaj) stringami (lub symbolami), a wartości mogą być dowolnego typu (liczby, stringi, funkcje, inne obiekty itd.).

Przykład literału obiektowego:

```javascript
const user = {
  id: 1,
  name: 'Alicja',
  active: true,
  greet() {
    console.log(`Cześć, nazywam się ${this.name}`);
  }
};

user.greet(); // Cześć, nazywam się Alicja
```

Obiekty są referencyjne — przypisanie do innej zmiennej nie kopiuje danych, a przekazuje referencję.

---

## 2. Prototypy i łańcuch prototypów (prototype chain)

JavaScript używa modelu dziedziczenia opartego na prototypach. Każdy obiekt ma referencję do swojego prototypu (wewnętrznie [[Prototype]]), z którego może dziedziczyć własności.

Tworzenie obiektu z prototypem:

```javascript
const proto = { hello() { console.log('hello'); } };
const obj = Object.create(proto);
obj.hello(); // dziedziczone z proto
```

Funkcje konstruktora i `prototype`:

```javascript
function Person(name) {
  this.name = name;
}
Person.prototype.greet = function() {
  console.log('Hi, I am ' + this.name);
};

const p = new Person('Jan');
p.greet();
```

Nowoczesna składnia klas (`class`) jest tylko cukrem składniowym nad prototypami:

```javascript
class PersonClass {
  constructor(name) { this.name = name; }
  greet() { console.log('Hi, I am ' + this.name); }
}
```

Ważne: prototypy są dynamiczne — można dodawać/metodować właściwości do prototypu w czasie działania programu.

---

## 3. Czym jest JSON i kto go wymyślił?

JSON (JavaScript Object Notation) to lekki format wymiany danych oparty składnią na notacji obiektowej JavaScript. Autorem, który wprowadził i spopularyzował JSON, jest Douglas Crockford. JSON został później ustandaryzowany (m.in. RFC 7159, potem RFC 8259 oraz ECMA-404).

JSON to format tekstowy — opisuje struktury danych (obiekty, tablice, liczby, stringi, wartości logiczne true/false, null) w sposób niezależny od języka, więc może być używany szeroko poza JavaScriptem.

---

## 4. Główne różnice: obiekt JS vs JSON

- JSON to **string** (tekst). Obiekt JS to struktura w pamięci.
- W JSON klucze muszą być zapisane w podwójnych cudzysłowach: { "name": "Alicja" }.
- JSON reprezentuje tylko: obiekty, tablice, liczby, stringi, true/false i null. Nie ma w nim funkcji, undefined, symboli ani referencji do obiektów (cyklicznych).
- JSON nie przechowa typu Date; daty są zwykle serializowane jako stringi (ISO 8601) i trzeba je z powrotem sparsować.

Przykład nieprawidłowej serializacji:

```javascript
const obj = { fn: () => 1, und: undefined, date: new Date() };
console.log(JSON.stringify(obj));
// Wynik nie zawiera fn ani und; date będzie stringiem ISO
```

---

## 5. Jak współpracować: JSON.parse i JSON.stringify

- JSON.stringify(obj) — zamienia obiekt JS na string JSON.
- JSON.parse(jsonString) — zamienia string JSON na obiekt JS.

Przykład:

```javascript
const data = { id: 1, name: 'Alicja' };
const json = JSON.stringify(data); // "{\"id\":1,\"name\":\"Alicja\"}"
const again = JSON.parse(json); // odtworzony obiekt
```

Opcje:
- JSON.stringify(value, replacer, space) — replacer może być funkcją lub tablicą kluczy; space formatuje wynik (ładniejsze wcięcia).
- JSON.parse(text, reviver) — reviver to funkcja, która pozwala transformować wartości podczas parsowania (np. odtworzyć obiekty Date).

Przykład z reviverem dla dat:

```javascript
const obj = { ts: new Date().toISOString() };
const json = JSON.stringify(obj);
const parsed = JSON.parse(json, (key, value) => {
  if (typeof value === 'string' && /\d{4}-\d{2}-\d{2}T/.test(value)) {
    return new Date(value);
  }
  return value;
});

console.log(parsed.ts instanceof Date); // true
```

---

## 6. Limitacje i pułapki przy użyciu JSON

- Brak obsługi funkcji i undefined — zostaną pominięte.
- Cykliczne odwołania powodują błąd przy stringify (TypeError: Converting circular structure to JSON).
- Straty typów (np. Set/Map, BigInt, Symbol) — trzeba je ręcznie serializować.
- Daty wymagają specjalnego traktowania (reviver / toJSON).
- JSON.stringify może zmienić kolejność kluczy (chociaż zwykle zachowuje porządek wstawiania w praktycznych implementacjach).

Jak radzić sobie z cyklicznością — prosty replacer, który zapamiętuje odwiedzone obiekty:

```javascript
function safeStringify(obj) {
  const seen = new WeakSet();
  return JSON.stringify(obj, (key, value) => {
    if (typeof value === 'object' && value !== null) {
      if (seen.has(value)) return; // pomiń cykliczne
      seen.add(value);
    }
    return value;
  });
}
```

---

## 7. Własne metody serializacji: toJSON

Obiekty mogą definiować metodę `toJSON`, którą `JSON.stringify` wywoła automatycznie, aby otrzymać reprezentację do serializacji.

```javascript
const obj = {
  x: 1,
  y: 2,
  toJSON() {
    return { x: this.x }; // tylko x zostanie zapisane
  }
};
console.log(JSON.stringify(obj)); // {"x":1}
```

---

## 8. Przykładowe zastosowania w Node.js i przeglądarce

- Przechowywanie konfiguracji w pliku JSON (fs.readFile / fs.writeFile + JSON.parse/stringify).
- Komunikacja klient‑serwer (API zwracające JSON).
- Szybkie klonowanie prostych obiektów: `const clone = JSON.parse(JSON.stringify(obj));` (uwaga na ograniczenia).

Przykład zapisu/odczytu w Node.js:

```javascript
const fs = require('fs').promises;

async function zapiszKonfig(konfig, path) {
  const json = JSON.stringify(konfig, null, 2);
  await fs.writeFile(path, json, 'utf8');
}

async function wczytajKonfig(path) {
  const text = await fs.readFile(path, 'utf8');
  return JSON.parse(text);
}
```

---

## 9. Dobre praktyki

- Używaj JSON dla wymiany danych i prostych struktur — nie do przechowywania funkcji ani stanów aplikacji.
- Przy serializacji kontroluj, co trafia do JSON (`replacer`, `toJSON`) i unikaj przypadkowego ujawniania wrażliwych danych.
- Rozważ formaty alternatywne, gdy potrzebujesz serializować Map/Set/BigInt (np. MessagePack, BSON) lub gdy wydajność i rozmiar mają znaczenie.
- Stosuj `reviver` do odtwarzania typów (np. Date) przy odczycie.
- Testuj scenariusze cykliczne i duże obiekty (może być kosztowne pamięciowo).

---

## 10. Podsumowanie

- Obiekt JS to struktura w pamięci z prototypowym dziedziczeniem; JSON to tekstowy format wymiany danych, stworzony i spopularyzowany przez Douglasa Crockforda i później ustandaryzowany.
- W JavaScript najczęściej używamy `JSON.stringify` i `JSON.parse` do konwersji między obiektami a JSON. Trzeba jednak pamiętać o ograniczeniach (funkcje, undefined, daty, cykliczność).
- Dzięki `replacer`, `reviver` i `toJSON` możemy kontrolować proces serializacji i deserializacji.

---

### Zadania do samodzielnego ćwiczenia

1. Zrób prosty plik konfiguracyjny `config.json`, wczytaj go i wypisz wartości w Node.js.
2. Zserializuj obiekt zawierający `Date`, a potem odtwórz datę przy pomocy `reviver`.
3. Spróbuj użyć `toJSON` aby ukryć wybrane pola podczas serializacji.

Powodzenia!
