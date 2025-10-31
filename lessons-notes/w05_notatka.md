# W05 — notatka

## 1. Streszczenie tematów
- Funkcja i cele baz danych: przechowywanie danych strukturalnych, szybkie wyszukiwanie dzięki indeksom, możliwość zapisu, edycji i usuwania rekordów.
- Typy baz danych: relacyjne (SQL) oraz alternatywy "no-SQL" i proste pliki JSON; relacyjne bazy umożliwiają korzystanie z języka SQL i indeksów.
- Porównanie: SQLite — lekka, plikowa implementacja SQL, nie wymaga serwera; MySQL i PostgreSQL — silniki serwerowe przeznaczone do większych aplikacji.
- Praca z bazą w Pythonie: połączenie (`connection`), kursor (`cursor`), wykonywanie zapytań (`execute`), pobieranie wyników (`fetchone`, `fetchall`), zatwierdzanie zmian (`commit`).
- Bezpieczeństwo: stosowanie zapytań parametryzowanych zamiast konkatenacji stringów w celu uniknięcia SQL Injection.
- Ograniczenia schematu: constrainty, np. UNIQUE (zapobiegają duplikatom); próba naruszenia ograniczeń powoduje wyjątek.
- Narzędzia wspomagające: Jupyter Notebook (połączenie kodu i dokumentacji) oraz Tkinter (proste GUI: okno, widgety, główna pętla `mainloop`).
- Przykładowe zastosowanie: prosty tracker czasu korzystający z SQLite i GUI do rejestrowania zdarzeń (start/stop, zapis timestampów).

## 2. Wymienione technologie (nazwa → opis)
- SQLite — plikowa, lekka baza SQL; łatwa do integracji w aplikacjach lokalnych i do szybkich prototypów.
- MySQL — serwerowa baza relacyjna, szeroko stosowana w aplikacjach webowych.
- PostgreSQL — zaawansowana serwerowa baza relacyjna, rozbudowane możliwości, silne wsparcie dla typów i funkcji.
- Jupyter Notebook — środowisko interaktywne łączące komórki kodu i opis (Markdown); użyteczne do eksperymentów i dokumentacji.
- Tkinter — biblioteka GUI dla Pythona do tworzenia podstawowych interfejsów (Label, Button, itp.).
- JSON — format wymiany danych i proste rozwiązanie do dumpów; przy dużych zbiorach wymaga parsowania całego pliku.

## 3. Angielskie słowa/wyrażenia (słowo — tłumaczenie — zastosowanie)
- SQL — Structured Query Language — język zapytań dla relacyjnych baz danych (SELECT, INSERT, UPDATE, DELETE).
- query — zapytanie — polecenie SQL wysyłane do bazy.
- cursor — kursor — obiekt do iteracji po wynikach zapytań (`execute` → `fetch*`).
- commit — zatwierdzenie — zapisanie zmian w bazie (transakcja).
- fetch / fetchone / fetchall — pobierz / pobierz jeden / pobierz wszystkie — metody odczytu wyników z kursora.
- unique — unikalny (constraint) — ograniczenie gwarantujące unikalność wartości w kolumnie.
- injection / SQL Injection — wstrzyknięcie SQL — podatność wynikająca z niebezpiecznego łączenia tekstu zapytań.
- notebook — (Jupyter) notatnik — środowisko mieszające kod i dokumentację.
- widget — widżet — element GUI (np. Label, Button).
- main loop — główna pętla aplikacji GUI obsługująca zdarzenia.
- f-string — sformatowany string (Python) — składnia do wstawiania wartości w łańcuchach: `f"...{val}..."`.
- tuple — tupla / krotka — niemutowalna sekwencja w Pythonie, używana m.in. do przekazywania parametrów do zapytań.

## 4. Techniki programistyczne i skróty klawiszowe
- Parametryzowane zapytania:
  - Użycie placeholderów (SQLite: `?`) i przekazywanie krotek z wartościami: `cursor.execute("INSERT INTO users(name) VALUES(?)", (name,))`.
  - Tupla jednoelementowa wymaga przecinka: `(value,)`.
- Wzorzec pracy z kursorem:
  - `cursor.execute(query, params)` → `rows = cursor.fetchall()` lub `row = cursor.fetchone()`.
- Zatwierdzanie zmian:
  - `connection.commit()` po operacjach INSERT/UPDATE/DELETE.
- Obsługa wyjątków przy naruszeniu constraintów (np. UNIQUE) lub przy operacjach mogących się nie powieść.
- F-stringi do czytelnego formatowania tekstu: `f"User: {user.name}"`.
- Type hints: stosowanie adnotacji typów (np. `conn: Connection`) ułatwia statyczne podpowiedzi w edytorach.
- Nazewnictwo: preferowane `snake_case` dla zmiennych i funkcji w Pythonie.

### Skróty (przykładowe, zależne od edytora):
- Alt+Enter — akcje kontekstowe / szybkie poprawki (np. dodanie importu, type hint).
- Ctrl+Q / F1 — szybka dokumentacja symbolu (może różnić się w zależności od środowiska).
- Ctrl+Shift+A — wyszukiwanie akcji/skrótów w edytorze.
- Ctrl+D — duplikowanie linii.
- Ctrl+/ — Zakomentuj/odkomentuj linie — szybkie tymczasowe wyłączanie fragmentów kodu.

## 5. Wskazówki i pułapki
- Nie łączyć fragmentów zapytań SQL przez konkatenację stringów — stosować zapytania parametryzowane.
- Przy testach bazodanowych uważać na istniejące constrainty (usuwanie testowych wpisów lub użycie transakcji z rollback).
- JSON jako "baza" jest prosty, ale nieefektywny przy dużych plikach (wymaga parsowania całości).
- Tupla jednoelementowa: pamiętać o przecinku `(val,)`.
- SELECT * zwraca wszystkie kolumny; jeśli potrzebne są konkretne kolumny, podawać je jawnie.
- Indeksy poprawiają szybkość zapytań wyszukujących, ale kosztują przy zapisie — stosować z rozwagą.

## 6. Materiały do nauki
- SQLite documentation: https://www.sqlite.org/docs.html
- Wprowadzenie do SQL (SELECT/WHERE/INSERT/UPDATE/DELETE)
- Jupyter Notebook — oficjalne materiały i tutoriale
- Tkinter — tutoriale dotyczące widgetów i mechanizmu zdarzeń

