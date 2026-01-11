
Podział kodu na pliki to kluczowy krok w nauce C++. Pozwala on oddzielić **interfejs** (to, co program widzi, że struktura posiada) od **implementacji** (tego, jak struktura faktycznie działa).


### 1. Plik nagłówkowy: `Gracz.h`

Tutaj tylko deklarujemy, co zawiera **struct** (lub **class**). 
Używamy tzw. *Header Guards* (`#ifndef`, `#define`, `#endif`), aby zapobiec wielokrotnemu wczytywaniu tego samego pliku.

```cpp
#ifndef GRACZ_H
#define GRACZ_H

#include <string>

struct Gracz {
    std::string nazwa;
    int punkty;

    // Tylko deklaracja (zapowiedź) funkcji
    void przedstawSie();
    void dodajPunkty(int ile);
};

#endif

```

### 2. Plik źródłowy (Logika): `Gracz.cpp`


```cpp
#include "Gracz.h"
#include <iostream>

// Definicja funkcji poza nagłówkiem
void Gracz::przedstawSie() {
    std::cout << "Czesc, jestem " << nazwa << " i mam " << punkty << " pkt!" << std::endl;
}

void Gracz::dodajPunkty(int ile) {
    if (ile > 0) {
        punkty += ile;
    }
}

```

### 3. Plik główny: `main.cpp`

To tutaj tworzysz obiekt i z niego korzystasz. Zauważ, że `main` nie widzi "wnętrzności" funkcji, widzi tylko to, co jest w pliku `.h`.

```cpp
#include "Gracz.h" // Dołączamy nasz nagłówek

int main() {
    Gracz zawodnik;
    zawodnik.nazwa = "Kamil";
    zawodnik.punkty = 100;

    zawodnik.dodajPunkty(50);
    zawodnik.przedstawSie();

    return 0;
}

```

---

### Dlaczego tak to dzielimy?

1. **Szybkość kompilacji**: Jeśli zmienisz coś tylko w pliku `.cpp` (np. zmienisz treść komunikatu w `przedstawSie`), kompilator musi przebudować tylko ten jeden plik, a nie cały wielki projekt.
2. **Czytelność**: Gdy otwierasz plik `.h`, od razu widzisz listę wszystkich pól i metod (taki "spis treści"), bez przedzierania się przez setki linii kodu samej logiki.
3. **Współpraca**: Możesz udostępnić komuś plik `.h`, żeby wiedział jak używać Twojego kodu, nie pokazując mu (lub nie pozwalając modyfikować) tego, jak on działa pod spodem.

## Budowanie Aplikacji

Budowanie programu złożonego z wielu plików to proces dwuetapowy: najpierw każdy plik `.cpp` jest zamieniany na tzw. plik obiektowy, a dopiero potem są one łączone w jeden gotowy program.

Oto jak to wygląda w praktyce przy użyciu popularnego kompilatora **g++** (część pakietu GCC):

### Jak to zbudować (krok po kroku)

Jeśli masz pliki `Gracz.h`, `Gracz.cpp` oraz `main.cpp`, wpisujesz w terminalu jedną komendę, która zrobi wszystko za Ciebie:

```bash
g++ main.cpp Gracz.cpp -o MojProgram

```

**Co się dzieje pod maską?**

1. **Kompilacja (`main.cpp` i `Gracz.cpp`)**: Kompilator czyta kod i zamienia go na język maszynowy (powstają niewidoczne pliki `.o` lub `.obj`). Zauważ, że nie wymieniamy pliku `.h` – on jest "wciągany" automatycznie przez `#include`.
2. **Linkowanie**: Kompilator widzi, że w `main.cpp` używasz funkcji `przedstawSie()`, ale jej tam nie ma. Szuka jej więc w `Gracz.cpp` (a właściwie w jego skompilowanej wersji) i "skleja" je razem.
3. **Wynik**: Powstaje plik wykonywalny `MojProgram` (lub `MojProgram.exe` na Windows).

---

### Różnica: Jeden plik vs. Wiele plików

Największą różnicą jest to, co dzieje się, gdy Twój projekt zaczyna rosnąć.

| Cecha | Jeden duży plik `.cpp` | Wiele plików (`.h` i `.cpp`) |
| --- | --- | --- |
| **Budowanie** | Kompilator zawsze musi czytać wszystko od zera. | Można kompilować tylko zmienione pliki (tzw. *Incremental Build*). |
| **Linkowanie** | Prawie nie występuje (wszystko jest w jednym miejscu). | **Kluczowy etap.** Musisz wskazać kompilatorowi wszystkie pliki źródłowe. |

---

### Dlaczego "linkowanie" jest takie ważne?

Gdy masz jeden plik, kompilator widzi wszystko naraz. Gdy masz wiele plików, każdy plik `.cpp` jest traktowany jak osobna wyspa.

* Kiedy kompiluje się `main.cpp`, kompilator "wierzy Ci na słowo" (dzięki plikowi `.h`), że funkcja `przedstawSie` istnieje gdzieś indziej.
* Dopiero **Linker** (ostatni etap budowania) sprawdza te obietnice. Jeśli zapomnisz dopisać `Gracz.cpp` do komendy kompilacji, Linker powie: *"Hej, obiecałeś mi funkcję przedstawSie, ale nigdzie jej nie widzę!"*.

### Podsumowanie różnicy w uruchamianiu

* **Jeden plik:** `g++ main.cpp -o program`
* **Wiele plików:** `g++ plik1.cpp plik2.cpp plik3.cpp -o program` (musisz wymienić wszystkie pliki źródłowe, które stworzyłeś).

---

### Skąd kompilator wie, która funkcja jest główna?

Kompilator (a właściwie Linker) szuka w całym projekcie dokładnie jednej funkcji o nazwie `main`. Jest to tzw. **punkt wejścia** (entry point).

Działa to tak:

1. Podczas kompilacji poszczególnych plików `.cpp` (np. `Gracz.cpp`, `main.cpp`), kompilator tylko odnotowuje, gdzie co jest zdefiniowane.
2. Na etapie **linkowania**, Linker szuka symbolu `_main` (lub podobnego, zależnie od systemu).
3. Jeśli znajdzie go dokładnie w jednym miejscu, ustawia go jako start programu. Jeśli nie znajdzie go wcale lub znajdzie dwa – przerwie pracę i wyrzuci błąd.

---

### Czy można mieć więcej niż jedną funkcję `main`?

Krótka odpowiedź brzmi: **W jednym programie (pliku wykonywalnym) może istnieć tylko jedna, globalna funkcja `main`.**

Możesz stworzyć funkcję o nazwie `main` wewnątrz własnej przestrzeni nazw (namespace), np. `MojaGra::main()`.
**ALE:** Dla kompilatora to **nie będzie** funkcja startowa. Będzie to po prostu zwykła funkcja, którą możesz wywołać, ale program i tak będzie szukał tej "prawdziwej", globalnej funkcji `main`.

```cpp
namespace MojaGra {
    void main() { /* To jest tylko zwykła funkcja */ }
}

int main() {
    // To jest JEDYNY prawdziwy punkt wejścia
    MojaGra::main(); 
    return 0;
}

```

### Kiedy jednak spotkasz "kilka mainów"?

Często w projektach studenckich lub bibliotekach zobaczysz wiele plików, z których każdy ma `main`. Jak to działa?

* Programista buduje z nich **osobne programy**.
* Na przykład: `g++ test_gracza.cpp Gracz.cpp -o test` (używa `main` z testów) oraz `g++ gra.cpp Gracz.cpp -o gra` (używa `main` z gry).

Podsumowując: w ramach **jednego budowanego pliku .exe**, zawsze musisz mieć **tylko jedną** funkcję `main`.

## Makefile

Kiedy projekt rośnie i masz już kilkanaście plików, wpisywanie ich ręcznie do konsoli staje się uciążliwe. Tutaj z pomocą przychodzi **Makefile**.

 **Makefile** to plik tekstowy, który zawiera zestaw instrukcji dla narzędzia `make`. Narzędzie to jest na tyle inteligentne, że samo sprawdza, które pliki zostały zmienione i kompiluje tylko to, co jest konieczne, dbając o odpowiednią kolejność.

---

### Jak wygląda prosty Makefile?

Stwórz w folderze z projektem plik o nazwie `Makefile` (bez żadnego rozszerzenia) i wklej do niego poniższą treść.

**Ważne:** W liniach z komendami (pod celami) musi znajdować się **znak tabulacji**, a nie spacje!

```makefile
# Zmienne, aby łatwiej było zmieniać ustawienia
CXX = g++
CXXFLAGS = -Wall -std=c++17

# Cel główny: buduje końcowy program
MojProgram: main.o Gracz.o
	$(CXX) $(CXXFLAGS) main.o Gracz.o -o MojProgram

# Jak zbudować main.o (zależy od main.cpp i nagłówka)
main.o: main.cpp Gracz.h
	$(CXX) $(CXXFLAGS) -c main.cpp

# Jak zbudować Gracz.o (zależy od Gracz.cpp i nagłówka)
Gracz.o: Gracz.cpp Gracz.h
	$(CXX) $(CXXFLAGS) -c Gracz.cpp

# Pomocnicza komenda do czyszczenia projektu
clean:
	rm -f *.o MojProgram

```

---

### Jak to działa w praktyce?

1. Wpisujesz w terminalu po prostu: `make`.
1. `make` patrzy na pierwszy zdefiniowany cel (w naszym przypadku jest to `MojProgram`). Pierwszy cel jest celem głównym zatem jak podasz samo `make` to tak jakbyś podał `make MojProgram`. 
1. Widzi, że potrzebuje plików `main.o` i `Gracz.o`.
1. Jeśli te pliki nie istnieją lub ich odpowiedniki `.cpp` są nowsze (bo coś w nich zmieniłeś), `make` najpierw wykona instrukcje budowania tych plików obiektowych.
1. Na koniec "linkuje" je w gotowy program.

---

### Czy musimy podawać pliki ręcznie?

W powyższym przykładzie podałem je ręcznie, ale w świecie C++ istnieją dwa sposoby, aby tego uniknąć:

#### 1. "Magiczne" zmienne w Makefile

Możesz użyć tzw. *wildcards*, które same wyszukają wszystkie pliki `.cpp` w folderze:

```makefile
SRCS = $(wildcard *.cpp)
OBJS = $(SRCS:.cpp=.o)

MojProgram: $(OBJS)
	$(CXX) $(OBJS) -o MojProgram

```

Dzięki temu, gdy dodasz nowy plik (np. `Przeciwnik.cpp`), `make` sam go zauważy i dołączy do procesu budowania.

#### 2. CMake – standard nowoczesnego C++

Dla profesjonalnych projektów Makefile bywa zbyt skomplikowany (szczególnie gdy chcesz, aby kod działał na Windows, Linux i Mac). Dlatego powstał **CMake**.

W CMake tworzysz plik `CMakeLists.txt`, który wygląda tak:

```cmake
cmake_minimum_required(VERSION 3.10)
project(MojaGra)

# Dodaj wszystkie pliki .cpp z folderu
file(GLOB SOURCES "*.cpp")

add_executable(MojProgram ${SOURCES})

```

CMake sam wygeneruje odpowiednie instrukcje budowania (Makefile na Linuxie lub projekt Visual Studio na Windowsie) w odpowiedniej kolejności.

---

### Podsumowanie: Dlaczego to jest lepsze?

* **Szybkość:** Jeśli zmienisz tylko jedną linię w `Gracz.cpp`, `make` skompiluje tylko ten plik. `main.cpp` zostanie nietknięty. To ogromna oszczędność czasu w dużych projektach.
* **Bezpieczeństwo:** Nie zapomnisz o żadnym pliku przy linkowaniu.
* **Wygoda:** Zamiast długiej komendy `g++ ...`, wpisujesz tylko `make`.

## CMake

Przejście z Makefile na **CMake** to skok w stronę profesjonalnych standardów. O ile Makefile jest instrukcją „jak to skompilować krok po kroku”, o tyle CMake jest opisem „z czego składa się projekt”.

Główna różnica polega na tym, że CMake nie kompiluje kodu bezpośrednio – on **generuje** pliki budowania (np. Makefile dla Linuxa lub projekt Visual Studio dla Windowsa).

---

### 1. Podstawowy plik: `CMakeLists.txt`

W folderze ze swoim projektem (tam, gdzie masz `main.cpp`, `Gracz.cpp` i `Gracz.h`) stwórz plik o nazwie `CMakeLists.txt`.

```cmake
# 1. Minimalna wersja CMake (bezpieczeństwo)
cmake_minimum_required(VERSION 3.10)

# 2. Nazwa Twojego projektu
project(MojaGra)

# 3. Ustawienie standardu C++ (np. C++17)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# 4. Tworzenie pliku wykonywalnego
# Składnia: add_executable(NAZWA_PROGRAMU PLIKI_ZRODLOWE)
add_executable(MojProgram main.cpp Gracz.cpp)

```

> **Zauważ:** W CMake nie musisz wymieniać plików `.h`. CMake sam je znajdzie, analizując instrukcje `#include` w plikach `.cpp`.

---

### 2. Jak uruchomić CMake? (Zasada "Out-of-source build")

Dobrą praktyką w CMake jest tworzenie osobnego folderu na pliki tymczasowe, aby nie robić bałaganu w kodzie źródłowym.

Wykonaj te komendy w terminalu (będąc w folderze projektu):

1. **Stwórz folder na budowanie:** `mkdir build`
2. **Wejdź do niego:** `cd build`
3. **Wygeneruj pliki budowania:** `cmake ..` (kropki oznaczają "szukaj CMakeLists.txt piętro wyżej")
4. **Skompiluj program:** `cmake --build .` (ta komenda jest uniwersalna i zadziała na każdym systemie)

Po tych krokach w folderze `build` znajdziesz swój gotowy program: `MojProgram`.

---

### 3. Dlaczego CMake jest lepszy od Makefile?

Oto kluczowe powody, dla których branża porzuciła czyste Makefile na rzecz CMake:

* **Wieloplatformowość:** Ten sam `CMakeLists.txt` zadziała na Windows (wygeneruje projekt `.sln`), Macu (Xcode) i Linuxie (Makefile).
* **Łatwe dodawanie bibliotek:** Jeśli będziesz chciał dodać np. bibliotekę graficzną SFML czy silnik fizyczny, w CMake zrobisz to kilkoma czytelnymi komendami, zamiast walczyć ze skomplikowanymi ścieżkami w Makefile.
* **Automatyzacja:** Jeśli dodasz nowy plik do projektu, nowoczesne edytory (jak VS Code czy CLion) same "odświeżą" konfigurację CMake za Ciebie.

---

### Czy muszę ręcznie dopisywać każdy nowy plik `.cpp`?

Wróćmy do Twojego pytania o automatyzację. Możesz kazać CMake samemu szukać plików, używając komendy `file(GLOB ...)`:

```cmake
file(GLOB SOURCES "*.cpp")
add_executable(MojProgram ${SOURCES})

```

## Użycie Bibliotek

Użycie zewnętrznej biblioteki w CMake to jeden z najsilniejszych argumentów za tym narzędziem. 

**Eigen** – to bardzo popularna, szybka i nowoczesna biblioteka numeryczna do operacji na macierzach i wektorach, która jest często używana w C++.

Biblioteka ta ma tę zaletę, że składa się z samych nagłówków (*header-only*), co ułatwia konfigurację.

### 1. Jak wygląda `CMakeLists.txt` z biblioteką?

Standardem w nowoczesnym CMake jest komenda `find_package`. Pozwala ona systemowi automatycznie zlokalizować bibliotekę zainstalowaną w systemie. (sic!)

```cmake
cmake_minimum_required(VERSION 3.10)
project(ObliczeniaNumeryczne)

set(CMAKE_CXX_STANDARD 17)

# 1. Szukamy biblioteki Eigen w systemie
find_package(Eigen3 REQUIRED)

# 2. Tworzymy program
add_executable(program_numeryczny main.cpp)

# 3. "Linkujemy" bibliotekę do naszego programu
# W CMake 'target_link_libraries' zajmuje się też ścieżkami do nagłówków
target_link_libraries(program_numeryczny PRIVATE Eigen3::Eigen)

```

### 2. Kod programu: `main.cpp`

Teraz w swoim kodzie możesz po prostu dołączyć bibliotekę, używając jej nazwy, a CMake zadba o to, by kompilator wiedział, gdzie ona leży.

```cpp
#include <iostream>
#include <Eigen/Dense> // Nagłówek biblioteki Eigen

int main() {
    // Używamy macierzy z biblioteki Eigen
    Eigen::Matrix2d macierz;
    macierz << 1, 2,
               3, 4;
               
    Eigen::Vector2d wektor(5, 10);
    
    // Wykonujemy operację numeryczną
    auto wynik = macierz * wektor;

    std::cout << "Wynik mnożenia macierzy przez wektor:\n" << wynik << std::endl;

    return 0;
}

```

### 3. Co się dzieje "pod maską"?

Kiedy używasz `find_package` i `target_link_libraries`:

1. **Lokalizacja:** CMake szuka w systemie pliku konfiguracyjnego biblioteki (np. `Eigen3Config.cmake`).
2. **Propagacja ustawień:** Biblioteki w CMake są traktowane jako "obiekty" (*Targets*). `Eigen3::Eigen` niesie ze sobą informacje o tym, jakie ścieżki do plików nagłówkowych (`include`) należy dodać do kompilacji Twojego programu.
3. **Czystość:** Nie musisz ręcznie wpisywać ścieżek typu `-I/usr/include/eigen3`. CMake robi to za Ciebie.

### A co jeśli nie mam biblioteki w systemie?

Jeśli nie chcesz instalować biblioteki globalnie, nowoczesny CMake pozwala ją pobrać automatycznie podczas budowania projektu za pomocą modułu **FetchContent**.

Wtedy Twój `CMakeLists.txt` wyglądałby tak:

```cmake
include(FetchContent)

FetchContent_Declare(
  eigen
  GIT_REPOSITORY https://gitlab.com/libeigen/eigen.git
  GIT_TAG 3.4.0
)
FetchContent_MakeAvailable(eigen)

# ... potem normalnie target_link_libraries ...
target_link_libraries(program_numeryczny PRIVATE Eigen3::Eigen)

```

**Podsumowując:**
Dzięki CMake i komendzie `target_link_libraries` zarządzanie bibliotekami staje się bardzo przejrzyste. Wystarczy, że powiesz CMake: "mój program potrzebuje Eigen", a on zajmie się resztą – niezależnie od tego, czy pracujesz na Windowsie, czy na Linuxie.

