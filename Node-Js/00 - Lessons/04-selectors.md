# Selektory — krótkie wprowadzenie

W tym pliku znajdziesz krótkie omówienie czym są selektory, skąd się wzięły, jak działają w kontekście CSS i DOM, oraz jak używać ich w JavaScript (preferując standardowe API). Na końcu jest krótki przykład w jQuery, ale nacisk kładziemy na natywne rozwiązania.

---

## 1. Skąd pochodzą selektory?

Selektory pochodzą z CSS — to reguły opisujące, które elementy w drzewie DOM mają pasować do danej reguły stylów (np. `.btn`, `#main`, `nav > ul > li:first-child`). Specyfikacja Selectors (wraz z Selectors API) jest rozwijana przez W3C i WHATWG jako część standardów przeglądarek.

W przeglądarkach powstało API, które pozwala używać tej samej składni selektorów z poziomu JavaScript: `querySelector` i `querySelectorAll` (Selectors API Level 1). Dzięki temu można znaleźć elementy w DOM za pomocą znanych z CSS wyrażeń.

---

## 2. Główne rodzaje selektorów (skrót)

- Selekcja po id: `#myId`
- Selekcja po klasie: `.my-class`
- Selekcja po tagu: `div`, `p`
- Selekcje atrybutowe: `[data-role="user"]`, `[type="button"]`
- Pseudoklasy: `:first-child`, `:nth-child(2n)`, `:hover` (CSS), `:not(.disabled)`
- Złożone selektory z relacjami: `parent > child`, `ancestor descendant`, `a + b`, `a ~ b`

UWAGA: nie wszystkie pseudoklasy mają sens w kontekście JS (np. `:hover` opisuje stan wizualny), ale większość strukturalnych pseudoklas (`:first-child`, `:nth-child`, `:not`) działa również w Selectors API.

---

## 3. Jak używać selektorów w standardowym JS

Najważniejsze metody:

- `document.querySelector(selector)` — zwraca pierwszy pasujący element lub `null`.
- `document.querySelectorAll(selector)` — zwraca statyczną NodeList wszystkich pasujących elementów.
- `element.querySelector(...)`, `element.querySelectorAll(...)` — ograniczenie wyszukiwania do poddrzewa elementu.
- Starsze alternatywy: `getElementById`, `getElementsByClassName`, `getElementsByTagName` (te ostatnie zwracają "live" kolekcje DOM, a nie statyczne NodeList).

Przykład prosty (vanilla JS):

```javascript
// pierwszy element z klasą .btn
const btn = document.querySelector('.btn');

// wszystkie linki wewnątrz nawigacji
const links = document.querySelectorAll('nav a');
links.forEach(a => console.log(a.href));

// wyszukiwanie w kontekście elementu
const container = document.getElementById('list');
const items = container.querySelectorAll('li.active');
```

Zwróć uwagę, że `querySelectorAll` zwraca NodeList, który w nowoczesnych przeglądarkach ma metodę `forEach`, ale nie ma wszystkich metod tablicowych (map/filter) — jeśli potrzebujesz tablicy:

```javascript
const arr = Array.from(document.querySelectorAll('.item'));
// lub
const arr2 = [...document.querySelectorAll('.item')];
```

---

## 4. Wydajność i dobre praktyki

- `getElementById` jest najszybszy, bo korzysta z wewnętrznej indeksacji id w przeglądarce.
- `querySelector`/`querySelectorAll` są elastyczne i wystarczająco szybkie dla większości zastosowań; nie używaj zbyt ogólnych selektorów w dużych drzewach DOM w pętli.
- Ogranicz zakres wyszukiwania (`element.querySelector`) zamiast zawsze skanować `document`.
- Cache'uj wyniki jeśli będziesz je wielokrotnie używać:

```javascript
const btn = document.querySelector('.submit');
btn.addEventListener('click', onSubmit);
```

- Unikaj wywoływania selektorów w gorących pętlach — zamiast tego zrób pojedyncze wyszukiwanie i operuj na wynikach.

---

## 5. Event delegation (delegowanie zdarzeń) — przykład użycia selektorów

Delegowanie to technika, w której nie przypisujemy nasłuchiwaczy do wielu elementów, lecz jednemu elementowi rodzicowi i sprawdzamy, czy event pochodzi od interesującego nas selektora.

```javascript
// przykład: kliknięcia w elementy listy
document.getElementById('list').addEventListener('click', (e) => {
  const btn = e.target.closest('button.delete');
  if (!btn) return; // ignorujemy kliknięcia poza selektorem

  const id = btn.dataset.id;
  deleteItem(id);
});
```

`Element.closest()` i `element.matches(selector)` to przydatne metody do pracy z selektorami w czasie obsługi zdarzeń.

---

## 6. Różnice między NodeList a HTMLCollection

- `querySelectorAll` zwraca statyczny `NodeList` — nie zmienia się automatycznie po modyfikacji DOM.
- `getElementsByClassName` i `getElementsByTagName` zwracają `HTMLCollection` (tzw. "live"), które aktualizuje się automatycznie po zmianach DOM.

Live kolekcje mogą zaskakiwać w pętlach (zmiana DOM podczas iteracji) — zwykle bezpieczniej użyć `querySelectorAll` i `Array.from`.

---

## 7. Przykłady zaawansowane (selektory atrybutowe, :not, :nth-child)

```javascript
// elementy z atrybutem data-role="user"
const users = document.querySelectorAll('[data-role="user"]');

// elementy które mają klasę .item, ale nie .disabled
const available = document.querySelectorAll('.item:not(.disabled)');

// trzeci element listy
const third = document.querySelector('ul li:nth-child(3)');
```

Pseudoklasy strukturalne (`:nth-child`, `:first-child`) działają dobrze, ale pamiętaj, że liczenie zaczyna się od 1.

---

## 8. Krótkie porównanie: jQuery vs natywny JS

jQuery zrobiło selektory bardzo popularnymi dzięki prostemu API `$('selector')`, które zwraca obiekt jQuery z wieloma użytecznymi metodami (chaining, manipulacja DOM, AJAX itp.).

Przykład w jQuery:

```javascript
// znajdź wszystkie przyciski i ukryj je
$('.btn').hide();

// delegowanie
$('#list').on('click', 'button.delete', function() {
  const id = $(this).data('id');
  deleteItem(id);
});
```

Współcześnie większość prostych operacji można napisać przy pomocy natywnego API bez jQuery. Jeśli zaczynasz nowy projekt, preferuj natywny kod: mniejszy rozmiar, brak zewnętrznych zależności i bardzo dobra kompatybilność przeglądarek.

---

## 9. Gdzie jeszcze selektory się przydają?

- Testy end-to-end i DOM-owe testy jednostkowe (np. use `data-testid` jako selektory stabilne względem zmian stylów).
- Parsowanie i przetwarzanie HTML (np. w Node.js z bibliotekami typu jsdom / cheerio — cheerio używa selektorów w stylu jQuery).
- Tworzenie narzędzi do migracji i skryptów automatycznych, które przeszukują DOM.

---

## 10. Dobre praktyki i wskazówki

- Preferuj selektory oparte na atrybutach `data-*` do celów skryptowych (np. `data-action`, `data-id`). Są one odporne na zmiany w stylach klas.
- Unikaj polegania na złożonych selektorach opartych na strukturze (np. `nav > ul > li:nth-child(2) > a`), bo layout może się zmienić.
- Daj priorytet `id` lub prostym klasom, gdy potrzebujesz szybko odnaleźć pojedynczy element.
- Używaj `matches` / `closest` / `dataset` tam, gdzie to sensowne.

---

## 11. Zadania do samodzielnego ćwiczenia

1. Napisz skrypt, który używa delegowania zdarzeń, aby obsłużyć kliknięcia w ich elementy listy (dodaj/usunąć).
2. Porównaj `querySelectorAll` i `getElementsByClassName` — w jaki sposób zachowują się przy dynamicznych zmianach DOM?
3. Stwórz przykładową stronę i użyj `data-` atrybutów jako selektorów do testów jednostkowych.

---

Plik gotowy. Jeśli chcesz, mogę dodać prosty `example.js` w katalogu z lekcjami demonstrujący powyższe przykłady, albo krótką ściągawkę CSS selector cheat-sheet na górę pliku.
