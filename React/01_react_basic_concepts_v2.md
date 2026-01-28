# React Deep Dive - Podstawowe i Zaawansowane Koncepcje

## 1. Czym jest Virtual DOM (VDOM)?

**Virtual DOM** to lekka kopia rzeczywistego drzewa DOM (Document Object Model), przechowywana w pamięci jako standardowe obiekty JavaScript.

*   **Działanie:** Kiedy zmienia się stan aplikacji, React tworzy nowe drzewo Virtual DOM. Następnie porównuje je z poprzednią wersją (proces ten nazywa się **"Diffing"** lub **"Reconciliation"**).
*   **Optymalizacja:** React wylicza minimalną liczbę operacji potrzebnych do zaktualizowania prawdziwego DOM, aby odzwierciedlił nowy stan. Operacje na prawdziwym DOM są kosztowne (powodują przeliczanie układu strony - reflow/repaint), więc VDOM drastycznie zwiększa wydajność poprzez ich minimalizację i grupowanie (batching).

## 2. Podstawowe Koncepcje

### Czym są Props (Properties)?
*   **Definicja:** Dane przekazywane do komponentu z góry (od rodzica).
*   **Niezmienność:** Propsy są **read-only** (tylko do odczytu). Komponent nie może modyfikować własnych propsów; może jedynie reagować na ich zmianę.
*   **Przeznaczenie:** Służą do konfiguracji komponentu i przekazywania danych.

**Przykład Props:**
```javascript
// Komponent Child otrzymuje props od rodzica
const Child = (props) => {
  return <h2>Moje imię to: {props.name}</h2>;
};

// Lub z destrukturyzacją
const Child = ({ name, age }) => {
  return <h2>Jestem {name} i mam {age} lat</h2>;
};

// Użycie
<Child name="Maria" age={30} />
```

### Inne kluczowe koncepcje:

1.  **State (Stan):** Wewnętrzna pamięć komponentu. W przeciwieństwie do propsów, stan jest zarządzany przez sam komponent i może być zmieniany, co powoduje re-render.

    ```javascript
    import { useState } from 'react';
    
    const Counter = () => {
      const [count, setCount] = useState(0);
      
      return (
        <div>
          <p>Licznik: {count}</p>
          <button onClick={() => setCount(count + 1)}>Zwiększ</button>
        </div>
      );
    };
    ```

2.  **Refs (Referencje):** Sposób na dostęp do bezpośrednich węzłów DOM lub przechowywanie wartości, które przetrwają renderowanie, ale ich zmiana nie powinna powodować re-renderu.

    ```javascript
    import { useRef } from 'react';
    
    const TextInput = () => {
      const inputRef = useRef(null);
      
      const focus = () => {
        inputRef.current.focus();
      };
      
      return (
        <>
          <input ref={inputRef} type="text" />
          <button onClick={focus}>Fokus na input</button>
        </>
      );
    };
    ```

3.  **Side Effects (Efekty uboczne):** Operacje wykraczające poza renderowanie widoku (np. pobieranie danych, subskrypcje, manipulacja DOM). Obsługiwane przez `useEffect`.

    ```javascript
    import { useEffect, useState } from 'react';
    
    const DataFetcher = () => {
      const [data, setData] = useState(null);
      const [loading, setLoading] = useState(true);
      
      useEffect(() => {
        // Pobieranie danych
        fetch('https://api.example.com/data')
          .then(res => res.json())
          .then(data => {
            setData(data);
            setLoading(false);
          });
      }, []); // Pusta tablica = efekt uruchamia się tylko raz
      
      if (loading) return <p>Ładowanie...</p>;
      return <p>{JSON.stringify(data)}</p>;
    };
    ```

4.  **Context:** Mechanizm przekazywania danych głęboko w dół drzewa komponentów bez konieczności przekazywania ich ręcznie przez każdy poziom ("props drilling").

    ```javascript
    import { createContext, useContext, useState } from 'react';
    
    const ThemeContext = createContext();
    
    const ThemeProvider = ({ children }) => {
      const [theme, setTheme] = useState('light');
      return (
        <ThemeContext.Provider value={{ theme, setTheme }}>
          {children}
        </ThemeContext.Provider>
      );
    };
    
    const ThemedComponent = () => {
      const { theme, setTheme } = useContext(ThemeContext);
      return (
        <div style={{ background: theme === 'light' ? '#fff' : '#000' }}>
          Obecny motyw: {theme}
          <button onClick={() => setTheme(theme === 'light' ? 'dark' : 'light')}>
            Zmień motyw
          </button>
        </div>
      );
    };
    ```

## 3. Deklaracja Komponentów

W nowoczesnym React używamy **Komponentów Funkcyjnych**. Są to zwykłe funkcje JavaScript, które zwracają JSX.

```javascript
// Deklaracja komponentu
const Welcome = ({ name, age }) => {
  return (
    <div className="card">
      <h1>Cześć, {name}</h1>
      <p>Masz {age} lat.</p>
    </div>
  );
};

// Użycie
<Welcome name="Alicja" age={25} />
```

## 4. JSX i jego tłumaczenie na JS

**JSX** (JavaScript XML) to "cukier składniowy", który pozwala pisać strukturę przypominającą HTML wewnątrz JavaScriptu. Przeglądarki nie rozumieją JSX, więc musi on zostać przetłumaczony (transpilowany, np. przez Babel) na zwykły JS.

**Przykład JSX:**
```javascript
const element = <h1 className="greeting">Hello, world!</h1>;
```

**Tłumaczenie na JS (Stary React):**
```javascript
const element = React.createElement(
  'h1',
  { className: 'greeting' },
  'Hello, world!'
);
```

**Tłumaczenie na JS (Nowy JSX Transform - React 17+):**
```javascript
import { jsx as _jsx } from 'react/jsx-runtime';
const element = _jsx('h1', { children: 'Hello, world!', className: 'greeting' });
```

## 5. Czym są Hooki i jak są zaimplementowane?

**Hooki** (np. `useState`, `useEffect`) to funkcje pozwalające "wpiąć się" w mechanizmy Reacta (stan, cykl życia) w komponentach funkcyjnych.

**Przykład useState:**
```javascript
import { useState } from 'react';

const LoginForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  
  const handleSubmit = (e) => {
    e.preventDefault();
    // Walidacja i logowanie
    if (email && password) {
      setIsLoggedIn(true);
    }
  };
  
  if (isLoggedIn) {
    return <p>Zalogowano jako {email}</p>;
  }
  
  return (
    <form onSubmit={handleSubmit}>
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        placeholder="Email"
      />
      <input
        type="password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        placeholder="Hasło"
      />
      <button type="submit">Zaloguj się</button>
    </form>
  );
};
```

### Implementacja (Uproszczony model koncepcyjny):
React nie "magicznie" wie, który stan należy do której zmiennej. Polega na **kolejności wywołań**.
Wewnątrz każdego komponentu (w strukturze zwanej `Fiber`) React przechowuje **listę (link list) lub tablicę** hooków.

Kiedy komponent się renderuje:
1.  React inicjalizuje wewnętrzny licznik (kursor) na `0`.
2.  Pierwsze wywołanie `useState` pobiera wartość z komórki `Hooks[0]` i przesuwa kursor na `1`.
3.  Drugie wywołanie `useState` pobiera wartość z `Hooks[1]` itd.

Dlatego **nie wolno** wywoływać hooków w pętlach (`if`, `for`), ponieważ zmiana kolejności wywołań sprawi, że `useState` zwróci stan przypisany do innej zmiennej.

## 6. Mechanizm Stale-Hook (Stale Closure)

Problem **Stale Closure** (nieświeże domknięcie) występuje, gdy funkcja (np. w `useEffect` lub callback eventu) "zapamiętuje" zmienne (stan/propsy) z momentu swojego utworzenia i nie ma dostępu do ich najnowszych wartości.

**Przykład problemu:**
```javascript
import { useState, useEffect } from 'react';

const BadExample = () => {
  const [count, setCount] = useState(0);
  
  // ❌ PROBLEM: Funkcja "zamknie" wartość count = 0
  // Nawet po kliknięciu, alert zawsze pokaże 0
  const handleClick = () => {
    setTimeout(() => {
      alert(`Licznik wynosi: ${count}`);
    }, 3000);
  };
  
  return (
    <div>
      <p>Licznik: {count}</p>
      <button onClick={() => setCount(count + 1)}>Zwiększ</button>
      <button onClick={handleClick}>Czekaj 3s i pokaż alert</button>
    </div>
  );
};
```

**Rozwiązanie za pomocą useRef:**
```javascript
import { useState, useRef } from 'react';

const GoodExample = () => {
  const [count, setCount] = useState(0);
  const countRef = useRef(count);
  
  const handleClick = () => {
    setTimeout(() => {
      // ✅ countRef.current zawsze ma najnowszą wartość
      alert(`Licznik wynosi: ${countRef.current}`);
    }, 3000);
  };
  
  // Aktualizuj ref za każdym razem gdy count się zmieni
  useEffect(() => {
    countRef.current = count;
  }, [count]);
  
  return (
    <div>
      <p>Licznik: {count}</p>
      <button onClick={() => setCount(count + 1)}>Zwiększ</button>
      <button onClick={handleClick}>Czekaj 3s i pokaż alert</button>
    </div>
  );
};
```

**Rozwiązanie za pomocą dependency array w useEffect:**
```javascript
import { useState, useEffect } from 'react';

const BestExample = () => {
  const [count, setCount] = useState(0);
  
  const handleClick = () => {
    // Efekt jest odtwarzany za każdym razem gdy count się zmienia
    // dzięki [count] w dependency array
    const timer = setTimeout(() => {
      // ✅ count ma zawsze aktualną wartość
      alert(`Licznik wynosi: ${count}`);
    }, 3000);
    
    return () => clearTimeout(timer); // Cleanup
  };
  
  return (
    <div>
      <p>Licznik: {count}</p>
      <button onClick={() => setCount(count + 1)}>Zwiększ</button>
      <button onClick={handleClick}>Czekaj 3s i pokaż alert</button>
    </div>
  );
};
```

**Co się dzieje:**
W JavaScript funkcje tworzą domknięcia (closures). Jeśli zdefiniujesz funkcję, która loguje `console.log(count)`, i `count` wynosiło wtedy `0`, ta funkcja "zamknie" w sobie wartość `0`. Nawet jeśli `count` w komponencie wzrośnie do `5`, ta konkretna instancja funkcji nadal widzi `0`.

**Rozwiązanie:**
Dlatego hooki (np. `useEffect`) wymagają **tablicy zależności (`dependency array`)**. Jeśli podasz `[count]`, React odtworzy funkcję/efekt za każdym razem, gdy `count` się zmieni, dzięki czemu domknięcie obejmie nową wartość.

## 7. Wyciek funkcji `setState`

**Pytanie:** Co się stanie, jeśli funkcja `setState` (np. `setCount` z `useState`) wycieknie na zewnątrz komponentu (np. zostanie przypisana do `window.updateMyComponent = setCount`)?

**Przykład wycieku:**
```javascript
import { useState } from 'react';

// Globalna referencja do setState
let globalSetCount;

const Counter = () => {
  const [count, setCount] = useState(0);
  
  // Wyciek! Przypisanie funkcji setState do obiektu globalnego
  globalSetCount = setCount;
  
  return (
    <div>
      <p>Licznik: {count}</p>
      <button onClick={() => setCount(count + 1)}>Zwiększ</button>
    </div>
  );
};

// W dowolnym miejscu w kodzie można teraz użyć:
// globalSetCount(5); // ✅ Działa! Aktualizuje komponent Counter

// W konsoli przeglądarki:
// window.globalSetCount(10); // ✅ Nadal działa!
```

**Odpowiedź:** React **będzie mógł jej użyć**.
*   Funkcja `setState` zwracana przez hook jest **stabilna**.
*   Jest ona trwale powiązana (zbind'owana) z konkretną instancją komponentu (konkretnym węzłem Fiber w pamięci Reacta), w którym została stworzona.
*   Wywołanie jej z dowolnego miejsca w aplikacji (nawet z konsoli przeglądarki) spowoduje zaplanowanie aktualizacji (re-renderu) **tego konkretnego komponentu**, do którego należy.

**Jednak:** Jeśli komponent został już odmontowany (usunięty z ekranu) i wywołamy jego `setState`:

```javascript
const App = () => {
  const [showCounter, setShowCounter] = useState(true);
  
  return (
    <div>
      {showCounter && <Counter />}
      <button onClick={() => setShowCounter(false)}>Usuń komponent</button>
    </div>
  );
};

// Workflow:
// 1. Komponent Counter jest mounted
// 2. globalSetCount = setCount (wyciek)
// 3. Klikasz "Usuń komponent" - Counter jest unmounted
// 4. Klikasz gdziekolwiek i callasz globalSetCount(5)
// 5. ⚠️ React wyrzuca ostrzeżenie: "Can't perform a React state update on an unmounted component"
// To ostrzeżenie chroni przed wyciekami pamięci
```

*Nota:* Jeśli komponent został już odmontowany (usunięty z ekranu) i wywołamy jego `setState`, React zazwyczaj rzuci ostrzeżenie ("Can't perform a React state update on an unmounted component"), ponieważ nie ma już czego aktualizować.

## 8. Diagram: Zmiana Props/State

Co się dzieje, gdy zmieniamy dane?

```text
[ TRIGGER ]                     [ RENDER PHASE ]                   [ COMMIT PHASE ]
Kliknięcie / Dane z API  --->   React wywołuje komponent   --->    React nakłada zmiany
      |                         funkcyjny ponownie.                  na prawdziwy DOM.
      v                                 |                                   |
Wywołanie setState()                    v                                   v
lub zmiana Propsów              Tworzenie nowego VDOM              Browser Paint (Rysowanie)
                                        |                                   |
                                        v                                   v
                                Porównanie z starym VDOM           Uruchomienie useEffect
                                (Diffing / Reconciliation)         (Side Effects)
```

## 9. Jak komponent dzieli się statem ze światem?

Stan jest domyślnie **lokalny** i prywatny. Aby się nim podzielić, stosuje się:

1.  **Lifting State Up (Podnoszenie stanu):**
    Przenosimy stan do najbliższego wspólnego rodzica obu komponentów. Rodzic przekazuje stan jednemu dziecku jako props, a drugiemu funkcję do zmiany tego stanu (też przez props).

    ```javascript
    // ❌ Było: Stan w każdym dziecku osobno (duplikacja)
    const Child1 = () => {
      const [value, setValue] = useState('');
      return <input value={value} onChange={(e) => setValue(e.target.value)} />;
    };
    
    // ✅ Jest: Podniesiony stan do rodzica
    const Parent = () => {
      const [sharedValue, setSharedValue] = useState('');
      
      return (
        <>
          <Child1 value={sharedValue} onChange={setSharedValue} />
          <Child2 value={sharedValue} />
        </>
      );
    };
    
    const Child1 = ({ value, onChange }) => (
      <input value={value} onChange={(e) => onChange(e.target.value)} />
    );
    
    const Child2 = ({ value }) => (
      <p>Współdzielona wartość: {value}</p>
    );
    ```

2.  **Callback Props:**
    Dziecko nie "udostępnia" stanu wprost, ale wywołuje funkcję przekazaną przez rodzica (`props.onDataChange(myInternalData)`), wysyłając dane w górę.

    ```javascript
    const Parent = () => {
      const handleChildData = (dataFromChild) => {
        console.log('Dane z dziecka:', dataFromChild);
      };
      
      return <ChildComponent onDataChange={handleChildData} />;
    };
    
    const ChildComponent = ({ onDataChange }) => {
      const [localData, setLocalData] = useState('');
      
      const handleChange = (e) => {
        const newValue = e.target.value;
        setLocalData(newValue);
        // Poinformuj rodzica o zmianie
        onDataChange(newValue);
      };
      
      return <input onChange={handleChange} value={localData} />;
    };
    ```

3.  **Context API:**
    Dla danych globalnych (motyw, użytkownik). `Provider` udostępnia stan, a dowolny komponent w drzewie może go odczytać używając `useContext`.

    ```javascript
    import { createContext, useContext, useState } from 'react';
    
    // Tworzenie kontekstu
    const UserContext = createContext();
    
    // Provider
    const UserProvider = ({ children }) => {
      const [user, setUser] = useState(null);
      const [isLoading, setIsLoading] = useState(false);
      
      const login = async (email, password) => {
        setIsLoading(true);
        try {
          const response = await fetch('/api/login', {
            method: 'POST',
            body: JSON.stringify({ email, password })
          });
          const userData = await response.json();
          setUser(userData);
        } finally {
          setIsLoading(false);
        }
      };
      
      const logout = () => setUser(null);
      
      return (
        <UserContext.Provider value={{ user, isLoading, login, logout }}>
          {children}
        </UserContext.Provider>
      );
    };
    
    // Komponent wykorzystujący kontekst
    const UserProfile = () => {
      const { user, logout } = useContext(UserContext);
      
      if (!user) return <p>Zaloguj się</p>;
      
      return (
        <div>
          <p>Witaj, {user.name}!</p>
          <button onClick={logout}>Wyloguj się</button>
        </div>
      );
    };
    
    // Użycie
    <UserProvider>
      <App />
    </UserProvider>
    ```

4.  **Zewnętrzne Store'y (Redux, Zustand, Recoil):**
    Stan trzymany jest całkowicie poza drzewem Reacta. Komponenty "subskrybują" zmiany w tym zewnętrznym obiekcie.

    ```javascript
    // Przykład z Zustand (prostsze niż Redux)
    import { create } from 'zustand';
    
    const useCounterStore = create((set) => ({
      count: 0,
      increment: () => set((state) => ({ count: state.count + 1 })),
      decrement: () => set((state) => ({ count: state.count - 1 })),
    }));
    
    // Komponent 1
    const Counter1 = () => {
      const { count, increment } = useCounterStore();
      return (
        <div>
          <p>Licznik: {count}</p>
          <button onClick={increment}>Zwiększ</button>
        </div>
      );
    };
    
    // Komponent 2 - widzi ten sam stan!
    const Counter2 = () => {
      const { count, decrement } = useCounterStore();
      return (
        <div>
          <p>Licznik: {count}</p>
          <button onClick={decrement}>Zmniejsz</button>
        </div>
      );
    };
    
    // Oba komponenty dzielą się tym samym stanem!
    // Zmiana w Counter1 -> aktualizacja w Counter2
    ```

