# Async / Await w JavaScript – praktyczne wprowadzenie

W tej lekcji krok po kroku przejdziemy od callbacków i Promise do `async/await`. Zobaczysz, **po co** powstało `async/await`, **jak z niego korzystać** i **jakie problemy rozwiązuje**.

---

## 1. Po co nam async/await?

JavaScript jest językiem **asynchronicznym** opartym na **pętli zdarzeń** (event loop). Operacje takie jak zapytania HTTP, odczyt plików, timery (`setTimeout`) nie zwracają wyniku od razu.

Najpierw mieliśmy **callbacki**, potem **Promise**, a dziś najwygodniejszą formą zapisu takiego kodu jest **`async/await`** – pozwala pisać kod, który *wygląda jak synchroniczny*, ale działa asynchronicznie.

---

## 2. Przypomnienie: callbacki (funkcje zwrotne)

**Callback** to funkcja, którą przekazujemy jako argument i wołamy ją później, gdy coś się wydarzy (np. gdy przyjdzie wynik zapytania).

```javascript
function pobierzDaneCallback(url, callback) {
    // Udajemy asynchroniczne pobieranie danych
    setTimeout(() => {
        const wynik = { url, data: "jakieś dane" };
        callback(null, wynik); // (błąd, wynik)
    }, 1000);
}

pobierzDaneCallback("/api/user", (err, data) => {
    if (err) {
        console.error("Błąd:", err);
        return;
    }
    console.log("Dane:", data);
});
```

Problem: gdy trzeba zrobić **kilka kroków po kolei** (pobierz → przetwórz → zapisz → loguj) kod szybko zamienia się w tzw. **callback hell** – zagnieżdżone funkcje, trudno się połapać.

---

## 3. Przypomnienie: Promise i łańcuchy `.then()`

**Promise** reprezentuje **wartość, która będzie dostępna w przyszłości** – albo zakończy się sukcesem (*resolved*), albo błędem (*rejected*).

```javascript
function pobierzDanePromise(url) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (!url) {
                reject(new Error("Brak URL"));
                return;
            }
            resolve({ url, data: "jakieś dane" });
        }, 1000);
    });
}

pobierzDanePromise("/api/user")
    .then(dane => {
        console.log("Dane:", dane);
        return dane.data.toUpperCase();
    })
    .then(przetworzone => {
        console.log("Przetworzone:", przetworzone);
    })
    .catch(err => {
        console.error("Błąd:", err);
    });
```

Promise jest już dużą poprawą względem callbacków, ale **przy większej liczbie kroków** łańcuch `.then()` nadal może być mało czytelny.

---

## 4. Problem: zagnieżdżony i mało czytelny kod asynchroniczny

Wyobraź sobie, że chcesz:
1. pobrać użytkownika,
2. pobrać jego zamówienia,
3. pobrać szczegóły pierwszego zamówienia.

Z użyciem `.then()` może to wyglądać tak (szkic):

```javascript
pobierzUzytkownika()
    .then(user => pobierzZamowienia(user.id))
    .then(orders => pobierzSzczegolyZamowienia(orders[0].id))
    .then(details => {
        console.log("Szczegóły:", details);
    })
    .catch(console.error);
```

Nie jest tragicznie, ale:
- trudniej wpleść **warunki** (`if`, `switch`),
- trudniej używać klasycznego `try`/`catch`,
- przy większej ilości logiki przepływ zaczyna być mało intuicyjny.

**Async/await** rozwiązuje ten problem.

---

## 5. Słowo kluczowe `async`

Dodając słowo **`async`** przed definicją funkcji mówimy JavaScriptowi:

> Ta funkcja **zawsze** zwróci `Promise`.

```javascript
async function pobierzCos() {
    return 42; // pod spodem: Promise.resolve(42)
}

const wynikPromise = pobierzCos();
console.log(wynikPromise instanceof Promise); // true
```

Funkcja `async` może zwracać:
- zwykłą wartość → zostanie opakowana w `Promise.resolve(...)`,
- rzucić błąd (`throw`) → powstanie `Promise.reject(...)`.

---

## 6. Słowo kluczowe `await`

Słowo **`await`** można używać **tylko wewnątrz funkcji `async`** (pomijając nowszy top-level await w modułach ESM).

```javascript
async function przyklad() {
    const wynik = await obietnica();
    console.log("Wynik:", wynik);
}
```

`await` powoduje, że **funkcja `async` pauzuje** w tym miejscu, aż Promise się rozwiąże (albo odrzuci):
- jeśli Promise zakończy się sukcesem → `await` zwraca jego wartość,
- jeśli Promise zostanie odrzucony → rzuci wyjątek, który możesz złapać w `try`/`catch`.

---

## 7. Z `.then()` na `async/await` – ten sam kod, prostszy zapis

Ten sam przykład z pobieraniem danych można zapisać na dwa sposoby:

### Wersja z `.then()`

```javascript
fetch("https://jsonplaceholder.typicode.com/todos/1")
    .then(response => {
        if (!response.ok) {
            throw new Error("HTTP " + response.status);
        }
        return response.json();
    })
    .then(todo => {
        console.log("TODO:", todo);
    })
    .catch(err => {
        console.error("Błąd:", err);
    });
```

### Wersja z `async/await`

```javascript
async function pobierzTodo() {
    try {
        const response = await fetch("https://jsonplaceholder.typicode.com/todos/1");

        if (!response.ok) {
            throw new Error("HTTP " + response.status);
        }

        const todo = await response.json();
        console.log("TODO:", todo);
    } catch (err) {
        console.error("Błąd:", err);
    }
}

pobierzTodo();
```

Kod z `async/await` **czyta się jak zwykłą procedurę**: krok po kroku.

---

## 8. Praktyczny przykład: `fetch` z async/await

Załóżmy, że mamy funkcję, która pobiera listę użytkowników z API i zwraca ją dalej.

```javascript
async function pobierzUzytkownikow() {
    const url = "https://jsonplaceholder.typicode.com/users";

    const response = await fetch(url);
    if (!response.ok) {
        throw new Error("Błąd pobierania: HTTP " + response.status);
    }

    const users = await response.json();
    return users;
}

async function uruchom() {
    try {
        const users = await pobierzUzytkownikow();
        console.log("Użytkownicy:", users.map(u => u.name));
    } catch (err) {
        console.error("Błąd w uruchom():", err.message);
    }
}

uruchom();
```

Zwróć uwagę, że:
- **`pobierzUzytkownikow`** jest `async` i zwraca `Promise`,
- w środku używamy **kilku `await` pod rząd**, ale kod jest liniowy.

---

## 9. Praktyczny przykład: funkcja `sleep` (opóźnienie)

Czasami chcesz „zaczekać X ms” w środku funkcji `async`.

Bez `async/await`:

```javascript
setTimeout(() => {
    console.log("Minęła 1 sekunda");
}, 1000);
```

Z własnym `sleep` + async/await:

```javascript
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function demoSleep() {
    console.log("Start");
    await sleep(1000); // czekamy 1 sekundę
    console.log("Minęła 1 sekunda");
    await sleep(500);
    console.log("Minęło kolejne 0.5 sekundy");
}

demoSleep();
```

Zauważ, że **`await` nie blokuje całego programu**, tylko pałzuje *daną funkcję async*. Inne rzeczy w tym czasie mogą się wykonywać.

---

## 10. Praktyczny przykład: pętle i async/await (sekwencyjnie vs równolegle)

### Sekwencyjne wykonanie (po kolei)

```javascript
async function pobierzSekwencyjnie(urls) {
    const wyniki = [];

    for (const url of urls) {
        const res = await fetch(url); // czekamy na każdy po kolei
        wyniki.push(await res.json());
    }

    return wyniki;
}
```

Każde `await` w pętli powoduje, że **kolejne żądanie zaczyna się dopiero po zakończeniu poprzedniego**.

### Równoległe wykonanie (szybciej)

```javascript
async function pobierzRownolegle(urls) {
    // Tworzymy wszystkie Promise na raz
    const promises = urls.map(url => fetch(url).then(r => r.json()));

    // Czekamy na wszystkie równolegle
    const wyniki = await Promise.all(promises);
    return wyniki;
}
```

Tutaj wszystkie `fetch` startują **od razu**, a `await Promise.all` czeka, aż wszystkie się zakończą. To zwykle jest **dużo szybsze** przy niezależnych operacjach.

---

## 11. Łączenie async/await z `Promise.all`

Wzorzec:

```javascript
async function pobierzWiele() {
    const urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2",
        "https://jsonplaceholder.typicode.com/todos/3",
    ];

    const zadania = urls.map(url => fetch(url));

    const responses = await Promise.all(zadania);
    const jsonPromises = responses.map(r => r.json());
    const todos = await Promise.all(jsonPromises);

    console.log("Todos:", todos);
}

pobierzWiele();
```

Ten sposób pozwala zachować **czytelność async/await** i jednocześnie wykorzystać **równoległe** wykonywanie Promise.

---

## 12. Obsługa błędów: `try` / `catch` z async/await

Największa zaleta async/await to możliwość użycia **klasycznego `try`/`catch`** do obsługi błędów.

```javascript
async function bezpiecznyFetch(url) {
    try {
        const res = await fetch(url);
        if (!res.ok) {
            throw new Error("HTTP " + res.status);
        }
        const data = await res.json();
        return data;
    } catch (err) {
        console.error("Błąd w bezpiecznyFetch:", err.message);
        // Możemy zdecydować, czy zwracamy wartość domyślną, czy rzucamy dalej
        throw err; // przekazujemy błąd wyżej
    }
}

async function main() {
    try {
        const data = await bezpiecznyFetch("https://jsonplaceholder.typicode.com/todos/1");
        console.log("Odebrane dane:", data);
    } catch (err) {
        console.error("Błąd w main():", err.message);
    }
}

main();
```

Dzięki temu **obsługa błędów wygląda tak samo jak w kodzie synchronicznym**.

---

## 13. Zalety async/await

Najważniejsze korzyści:

- **Czytelność** – kod wygląda jak synchroniczny, łatwiej go śledzić.
- **Mniej zagnieżdżeń** – mniej callbacków i `.then()`.
- **Łatwa obsługa błędów** – klasyczne `try`/`catch`.
- **Lepsza współpraca z pętlami i warunkami** – `for`, `if`, `switch` itp.
- Nadal opiera się na **Promise** – nie jest to inny mechanizm, tylko „cukier składniowy”.

---

## 14. Typowe problemy i pułapki

### 14.1. Zapomniany `await`

```javascript
async function pobierz() {
    return 42;
}

async function zlyPrzyklad() {
    const wynik = pobierz(); // brak await!
    console.log(wynik); // Promise, a nie 42
}

zlyPrzyklad();
```

Pamiętaj: **funkcja `async` zawsze zwraca Promise**. Jeśli chcesz wartość – użyj `await`.

---

### 14.2. Zbyt sekwencyjne `await` w pętlach

```javascript
async function wolno(urls) {
    for (const url of urls) {
        const res = await fetch(url); // czekasz na każde po kolei
        console.log("Gotowe:", url, res.status);
    }
}
```

Jeśli żądania są niezależne, lepiej:

```javascript
async function szybciej(urls) {
    const zadania = urls.map(url => fetch(url));
    const wyniki = await Promise.all(zadania);
    console.log("Wszystko gotowe", wyniki.length);
}
```

---

### 14.3. Brak `try`/`catch` – zgubione błędy

Jeśli nie używasz `try`/`catch` i nie dodasz `.catch()` na Promise, błędy mogą być słabo widoczne.

```javascript
async function ryzykowne() {
    const res = await fetch("https://zly-adres");
    return res.json();
}

ryzykowne(); // błąd może się pojawić jako "UnhandledPromiseRejection"
```

Lepiej zawsze łapać błędy na jakimś poziomie:

```javascript
ryzykowne().catch(err => {
    console.error("Błąd w ryzykowne():", err);
});
```

---

## 15. Podsumowanie – co zapamiętać

- **`async`** przed funkcją oznacza, że **zwraca ona Promise**.
- **`await`** zatrzymuje wykonanie funkcji `async`, aż Promise się rozwiąże.
- Async/await:
  - upraszcza kod asynchroniczny,
  - pozwala pisać go **liniowo**,
  - świetnie współpracuje z `try`/`catch` i klasycznymi konstrukcjami (`if`, `for`).
- To nadal są **Promise**, tylko w wygodniejszej formie.

---

## 16. Zadania do samodzielnego ćwiczenia

1. **Przepisz kod z `.then()` na async/await**  
   Weź dowolny przykład z poprzednich lekcji lub dokumentacji (`fetch`, odczyt pliku z `fs.promises` w Node) i przepisać go na async/await.

2. **Napisz swoją funkcję `sleep`**  
   Utwórz funkcję `sleep(ms)` i użyj jej w `async function`, aby:
   - wypisać licznik od 5 do 0,
   - zrobić 1 sekundę przerwy między kolejnymi liczbami.

3. **Pobierz równolegle kilka zasobów**  
   Napisz funkcję, która dostaje tablicę URL-i, pobiera je równolegle (`Promise.all`) i zwraca tablicę wyników. Dodaj obsługę błędów (`try`/`catch`).

Eksperymentuj – zmieniaj czasy w `sleep`, psuj adresy URL, usuwaj `await` i zobacz, co się dzieje. Tak najszybciej zrozumiesz async/await w praktyce.
