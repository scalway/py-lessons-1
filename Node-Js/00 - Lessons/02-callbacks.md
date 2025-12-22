# Callbacki w JavaScript — co to jest i jak z nich korzystać

W tej lekcji wyjaśnimy, czym są callbacki (funkcje zwrotne), jakie mają zastosowania w JavaScript (przeglądarka i Node.js), pokażemy praktyczne przykłady i wypiszemy dobre praktyki oraz pułapki, których warto unikać.

---

## 1. Czym jest callback?

Callback (funkcja zwrotna) to po prostu funkcja przekazana jako argument do innej funkcji, która zostanie wywołana później — zwykle po zakończeniu pewnej operacji.

Prosty przykład (synchronny):

```javascript
function wykonajOperacje(x, callback) {
  const wynik = x * 2;
  callback(wynik);
}

wykonajOperacje(3, result => {
  console.log('Wynik:', result); // Wynik: 6
});
```

Callbacki są fundamentem asynchroniczności w JavaScript — wiele API (timery, zdarzenia DOM, stare API Node) używa callbacków do powiadamiania o wyniku operacji.

---

## 2. Przykłady callbacków — asynchroniczne użycie

1) setTimeout (przeglądarka / Node):

```javascript
console.log('Start');
setTimeout(() => {
  console.log('Po 1 sekundzie');
}, 1000);
console.log('Koniec');
```

Wyjście:
Start
Koniec
Po 1 sekundzie

2) Listener zdarzeń w przeglądarce:

```javascript
const btn = document.querySelector('#myBtn');
btn.addEventListener('click', function (event) {
  console.log('Kliknięto przycisk!', event);
});
```

3) Node.js — wzorzec "error-first callback" (standardowy w wielu API):

```javascript
const fs = require('fs');

fs.readFile('./plik.txt', 'utf8', (err, data) => {
  if (err) {
    console.error('Błąd odczytu pliku:', err);
    return;
  }
  console.log('Zawartość pliku:', data);
});
```

Wzorzec error-first polega na tym, że pierwszy argument callbacka to błąd (lub null), a drugi to wynik. Dzięki temu łatwo rozróżnić sukces od niepowodzenia.

---

## 3. Typowe wzorce i idiomy

- Error-first callbacks: (err, result) => {}
- Callbacky jednorazowe vs wielokrotnego użycia (event listener): `addEventListener` może być wywołany wiele razy; `once` w Node/event emitter pozwala na jednokrotne wywołanie.
- Zamykanie wartości w callbackach (closure) — callback ma dostęp do zewnętrznych zmiennych w momencie definicji.

Przykład wykorzystania closure:

```javascript
function makeCounter() {
  let i = 0;
  return () => ++i;
}

const next = makeCounter();
console.log(next()); // 1
console.log(next()); // 2
```

---

## 4. Callback hell — kiedy callbacki stają się problemem

Przy złożonych sekwencjach asynchronicznych, gdy operacje zależą od wyników poprzednich, callbacki łatwo prowadzą do głębokich zagnieżdżeń:

```javascript
pobierzUsera(id, (err, user) => {
  if (err) return handle(err);
  pobierzZamowienia(user.id, (err, orders) => {
    if (err) return handle(err);
    pobierzSzczegoly(orders[0].id, (err, details) => {
      if (err) return handle(err);
      // ...
    });
  });
});
```

Kod staje się trudny do czytania i utrzymania. Trudniej też wprowadzać warunki, pętle czy klasyczną obsługę wyjątków.

---

## 5. Jak radzić sobie z callback hell

- Modularizuj: wydzielaj kroki do osobnych funkcji zamiast zagnieżdżać je inline.
- Używaj nazwanych funkcji zamiast dużych anonimowych bloków.
- Przemyśl przepływ sterowania (early return przy błędach).
- Tam, gdzie to możliwe, używaj Promise / async/await (konwersja callback → Promise).

Przykład refaktoryzacji (nazwane funkcje):

```javascript
function onDetails(err, details) {
  if (err) return handle(err);
  console.log('Details', details);
}

function onOrders(err, orders) {
  if (err) return handle(err);
  pobierzSzczegoly(orders[0].id, onDetails);
}

pobierzUsera(id, (err, user) => {
  if (err) return handle(err);
  pobierzZamowienia(user.id, onOrders);
});
```

---

## 6. Konwersja callback → Promise (przykład: util.promisify)

W Node.js można łatwo zamienić API oparte na callbackach na Promise, np. za pomocą `util.promisify`.

```javascript
const fs = require('fs');
const util = require('util');
const readFile = util.promisify(fs.readFile);

async function demo() {
  try {
    const data = await readFile('./plik.txt', 'utf8');
    console.log('Zawartość:', data);
  } catch (err) {
    console.error('Błąd:', err);
  }
}

demo();
```

Ręczna konwersja:

```javascript
function readFilePromise(path, encoding) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, encoding, (err, data) => {
      if (err) return reject(err);
      resolve(data);
    });
  });
}
```

---

## 7. Dobre praktyki przy użyciu callbacków

- Używaj wzorca "error-first" w API, gdzie to ma sens: `(err, result) => {}`.
- Zawsze obsługuj błąd jak najwcześniej (early return) i nie zakopuj błędów.
- Unikaj nadmiernego zagnieżdżania — wydzielaj logikę do osobnych funkcji.
- Nadaj callbackom sensowne nazwy (np. `onData`, `onError`, `handleResult`).
- Zapobiegaj podwójnemu wywołaniu callbacka (np. poprzez flagi lub `once`).
- Dokumentuj kontrakt funkcji: jakie argumenty callback otrzymuje i kiedy jest wywoływany.
- Rozważ użycie `Promise` / `async-await` dla bardziej czytelnego przepływu.
- W Node.js rozważ `util.promisify` lub biblioteki, które oferują Promise zamiast callbacków.
- Przy event listenerach pamiętaj o usuwaniu niepotrzebnych listenerów (`removeEventListener`, `emitter.off`) aby uniknąć wycieków pamięci.

---

## 8. Pułapki i często popełniane błędy

- Podwójne wywołanie callbacka — np. najpierw reject/return, a potem nadal wywołujesz callback.
- Brak obsługi błędów → Unhandled errors.
- Mieszanie stylów: callback + Promise w tym samym API może mylić użytkownika.
- Utrata kontekstu `this` w callbackach — używaj arrow functions lub `bind` jeśli potrzebujesz zachować kontekst.

Przykład utraty kontekstu:

```javascript
const obj = {
  x: 10,
  logX() {
    console.log(this.x);
  }
};

setTimeout(obj.logX, 1000); // undefined lub błąd, bo this nie jest obj
setTimeout(() => obj.logX(), 1000); // poprawnie: 10
```

---

## 9. Kiedy zostawić callbacki?

Callbacki nadal mają sens:
- w prostych, jednorazowych wywołaniach,
- w API, które ma charakter zdarzeniowy (emitery, event listenery),
- gdy zależy nam na minimalnym narzucie i kompatybilności wstecznej,
- w sytuacjach o niskim poziomie (niektóre biblioteki i legacy code).

---

## 10. Podsumowanie

Callbacki to podstawowy mechanizm w JavaScript do pracy z asynchronicznością i zdarzeniami. Są proste i szybkie, ale przy złożonym przepływie logicznym prowadzą do trudnej do utrzymania struktury kodu. Dobre praktyki (error-first, modularność, nazwy funkcji) oraz migracja do Promise/async-await w miejscach złożonych operacji znacznie poprawiają czytelność i niezawodność kodu.

---

## 11. Zadania do samodzielnego ćwiczenia

1. Napisz funkcję `readFileCallback(path, cb)` w Node.js która czyta plik i zwraca wynik przez callback w stylu `(err, data)`.
2. Zaimplementuj kilka kroków asynchronicznych (pobierz dane → przetwórz → zapisz) najpierw używając callbacków, a potem przepisać to do Promise/async-await.
3. Znajdź istniejący fragment kodu z callbackami i zrefaktoryzuj go, wydzielając nazwy funkcji zamiast anonimowych callbacków.

Powodzenia!
