# Object Destructuring w JavaScript

---

## 1. Po co nam Object Destructuring?

Wyobraź sobie, że masz obiekt ze szczegółami użytkownika:

```javascript
const user = {
    name: "Anna",
    age: 28,
    email: "anna@example.com",
    city: "Warszawa"
};
```

Tradycyjnie, aby dostać się do poszczególnych właściwości:

```javascript
const name = user.name;
const email = user.email;
const age = user.age;
```

To działa, ale jest **powtarzalne** i **nieczytelne**. Object Destructuring pozwala zrobić to elegancko:

```javascript
const { name, email, age } = user;

console.log(name);   // "Anna"
console.log(email);  // "anna@example.com"
console.log(age);    // 28
```

**Jedna linijka zamiast trzech!** A kod jest **bardziej czytelny**.

---

## 2. Podstawowa składnia Object Destructuring

### 2.1. Destrukturyzacja podstawowych właściwości

```javascript
const product = {
    id: 1,
    title: "Laptop",
    price: 2999,
    inStock: true
};

// Destrukturyzacja
const { id, title, price } = product;

console.log(id);     // 1
console.log(title);  // "Laptop"
console.log(price);  // 2999
```

### 2.2. Destrukturyzacja z aliasami (zmiana nazw)

Czasem chcesz dać zmiennym inne nazwy:

```javascript
const { id: productId, title: productName, price: cost } = product;

console.log(productId);   // 1
console.log(productName); // "Laptop"
console.log(cost);        // 2999
```

Składnia: `{ stara_nazwa: nowa_nazwa }`

### 2.3. Wartości domyślne

Co zrobić, jeśli właściwość nie istnieje w obiekcie?

```javascript
const user = { name: "Jan" };

// Bez wartości domyślnej
const { name, age } = user;
console.log(age); // undefined

// Z wartościami domyślnymi
const { name: userName, age: userAge = 18 } = user;
console.log(userName);  // "Jan"
console.log(userAge);   // 18 (domyślna wartość)
```

---

## 3. Praktyczne przykłady

### 3.1. Destrukturyzacja parametrów funkcji

Zamiast:

```javascript
function printUser(user) {
    console.log(user.name);
    console.log(user.email);
}

printUser({ name: "Anna", email: "anna@example.com" });
```

Możesz:

```javascript
function printUser({ name, email }) {
    console.log(name);  // "Anna"
    console.log(email); // "anna@example.com"
}

printUser({ name: "Anna", email: "anna@example.com" });
```

Znacznie **czytelniej** – od razu wiesz, jakie parametry funkcja potrzebuje!

### 3.2. Destrukturyzacja z wartościami domyślnymi w parametrach

```javascript
function createUser({ name, age = 18, role = "user" } = {}) {
    return {
        name,
        age,
        role,
        createdAt: new Date()
    };
}

console.log(createUser({ name: "Tomek" }));
// { name: "Tomek", age: 18, role: "user", createdAt: ... }

console.log(createUser({ name: "Admin", role: "admin" }));
// { name: "Admin", age: 18, role: "admin", createdAt: ... }
```

### 3.3. Destrukturyzacja zagnieżdżonych obiektów

```javascript
const employee = {
    id: 1,
    name: "Paweł",
    address: {
        street: "Marszałkowska 10",
        city: "Warszawa",
        zipcode: "00-021"
    }
};

// Bez destrukturyzacji
const street = employee.address.street;

// Z destrukturyzacją
const { address: { street, city } } = employee;
console.log(street); // "Marszałkowska 10"
console.log(city);   // "Warszawa"
```

### 3.4. Pozostałe właściwości (rest operator `...`)

Czasem chcesz wydobyć kilka właściwości, a resztę trzymać w jednym obiekcie:

```javascript
const person = {
    name: "Karol",
    age: 30,
    email: "karol@example.com",
    phone: "123456789",
    city: "Kraków"
};

const { name, age, ...rest } = person;

console.log(name);  // "Karol"
console.log(age);   // 30
console.log(rest);  // { email: "karol@example.com", phone: "123456789", city: "Kraków" }
```

---

## 4. Array Destructuring (destrukturyzacja tablic)

Object Destructuring ma bliźniaka – **Array Destructuring**. Działa podobnie, ale dla tablic:

### 4.1. Podstawowa destrukturyzacja tablicy

```javascript
const colors = ["red", "green", "blue"];

// Tradycyjnie
const color1 = colors[0];
const color2 = colors[1];

// Z destrukturyzacją
const [first, second, third] = colors;
console.log(first);  // "red"
console.log(second); // "green"
console.log(third);  // "blue"
```

### 4.2. Pomijanie elementów

```javascript
const [red, , blue] = colors; // pomijamy green (middle element)
console.log(red);  // "red"
console.log(blue); // "blue"
```

### 4.3. Rest operator w tablicach

```javascript
const [head, ...tail] = [1, 2, 3, 4, 5];
console.log(head); // 1
console.log(tail); // [2, 3, 4, 5]
```

### 4.4. Swap – zamiana wartości

```javascript
let a = 5;
let b = 10;

[a, b] = [b, a];

console.log(a); // 10
console.log(b); // 5
```

---

## 5. Object Destructuring w React

### 5.1. Destrukturyzacja props w komponencie funkcyjnym

React wykorzystuje Object Destructuring bardzo intensywnie. Oto komponent bez destrukturyzacji:

```javascript
function UserCard(props) {
    return (
        <div>
            <h1>{props.name}</h1>
            <p>Email: {props.email}</p>
            <p>Wiek: {props.age}</p>
        </div>
    );
}
```

To działa, ale jest **mało czytelne** – nie wiadomo od razu, jakie props potrzebuje komponent.

Z **Object Destructuring**:

```javascript
function UserCard({ name, email, age }) {
    return (
        <div>
            <h1>{name}</h1>
            <p>Email: {email}</p>
            <p>Wiek: {age}</p>
        </div>
    );
}
```

Teraz od razu widać, jakie `props` komponent przyjmuje! 🎯

### 5.2. Destrukturyzacja props z wartościami domyślnymi

```javascript
function Button({ label = "Kliknij", onClick = () => {}, disabled = false }) {
    return (
        <button onClick={onClick} disabled={disabled}>
            {label}
        </button>
    );
}

// Użycie
<Button label="Wyślij" onClick={handleSubmit} />
// lub skrótowo, korzystając z domyślnych wartości:
<Button />
```

### 5.3. Destrukturyzacja `children` i `className`

```javascript
function Card({ children, className = "" }) {
    return (
        <div className={`card ${className}`}>
            {children}
        </div>
    );
}

// Użycie
<Card className="dark">
    <h2>Zawartość karty</h2>
</Card>
```

### 5.4. Destrukturyzacja state w hookach

#### useState

```javascript
import { useState } from "react";

function Counter() {
    const [count, setCount] = useState(0);
    const [isActive, setIsActive] = useState(false);

    return (
        <div>
            <p>Licznik: {count}</p>
            <button onClick={() => setCount(count + 1)}>Zwiększ</button>
            <button onClick={() => setIsActive(!isActive)}>
                {isActive ? "Aktywny" : "Nieaktywny"}
            </button>
        </div>
    );
}
```

#### useContext

**`useContext`** – hook, który pozwala Ci uzyskać dostęp do wartości z **Context API**. Context to sposób na przesyłanie danych (jak `props`) bez konieczności przekazywania ich przez każdy komponent po drodze (tzw. *prop drilling*).

`useContext` przyjmuje obiekt Context i zwraca jego bieżącą wartość. Możesz następnie destrukturyzować dane z tej wartości.

```javascript
import { createContext, useContext } from "react";

const ThemeContext = createContext();

function MyComponent() {
    // useContext pobiera wartość z ThemeContext
    // i od razu destrukturyzujemy { theme, toggleTheme }
    const { theme, toggleTheme } = useContext(ThemeContext);

    return <button onClick={toggleTheme}>Temat: {theme}</button>;
}
```

**Jak to działa:**
1. `ThemeContext` przechowuje dane dostępne wszędzie w aplikacji.
2. `useContext(ThemeContext)` pobiera aktualną wartość z tego Context.
3. Destrukturyzacja `{ theme, toggleTheme }` rozpakuje dane z tej wartości.
4. Teraz możemy używać `theme` i `toggleTheme` bezpośrednio w komponencie.

**Praktyczny przykład z Provider:**

```javascript
import { createContext, useContext, useState } from "react";

const ThemeContext = createContext();

// Provider – komponent, który dostarcza dane
export function ThemeProvider({ children }) {
    const [theme, setTheme] = useState("light");

    const toggleTheme = () => {
        setTheme(prev => prev === "light" ? "dark" : "light");
    };

    return (
        <ThemeContext.Provider value={{ theme, toggleTheme }}>
            {children}
        </ThemeContext.Provider>
    );
}

// Komponent, który konsumuje dane z Context
function MyComponent() {
    const { theme, toggleTheme } = useContext(ThemeContext);

    return (
        <div className={`container ${theme}`}>
            <p>Aktualny temat: {theme}</p>
            <button onClick={toggleTheme}>Zmień temat</button>
        </div>
    );
}

// Użycie w aplikacji
function App() {
    return (
        <ThemeProvider>
            <MyComponent />
        </ThemeProvider>
    );
}
```

**Korzyści:**
- Nie musisz przekazywać `props` przez wiele poziomów komponentów.
- Dane (jak temat, autentykacja, ustawienia) są dostępne wszędzie.
- Kod jest czystszy i łatwiejszy do utrzymania.

### 5.5. Destrukturyzacja event objects

```javascript
function SearchInput() {
    function handleChange(event) {
        console.log(event.target.value);
    }

    // Lub z destrukturyzacją
    function handleChangeDestructured({ target: { value } }) {
        console.log(value);
    }

    return (
        <>
            <input onChange={handleChange} placeholder="Szukaj..." />
            <input onChange={handleChangeDestructured} placeholder="Szukaj..." />
        </>
    );
}
```

### 5.6. Destrukturyzacja API response

Bardzo częste w React:

```javascript
import { useState, useEffect } from "react";

function UserList() {
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch("https://api.example.com/users")
            .then(res => res.json())
            .then(data => {
                setUsers(data);
                setLoading(false);
            })
            .catch(err => {
                setError(err);
                setLoading(false);
            });
    }, []);

    // Lub elegancko z destrukturyzacją w funkcji:
    useEffect(() => {
        async function loadUsers() {
            try {
                const res = await fetch("https://api.example.com/users");
                const { data, success } = await res.json(); // destrukturyzacja!

                if (success) {
                    setUsers(data);
                }
            } catch (err) {
                setError(err);
            } finally {
                setLoading(false);
            }
        }

        loadUsers();
    }, []);

    if (loading) return <p>Ładowanie...</p>;
    if (error) return <p>Błąd: {error.message}</p>;

    return (
        <ul>
            {users.map(({ id, name, email }) => (
                <li key={id}>
                    {name} ({email})
                </li>
            ))}
        </ul>
    );
}
```

### 5.7. Praktyczny przykład: Komponent formularza

```javascript
import { useState } from "react";

function LoginForm() {
    const [formData, setFormData] = useState({
        email: "",
        password: "",
        rememberMe: false
    });

    // Destrukturyzacja state
    const { email, password, rememberMe } = formData;

    function handleChange({ target: { name, value, type, checked } }) {
        setFormData(prev => ({
            ...prev,
            [name]: type === "checkbox" ? checked : value
        }));
    }

    async function handleSubmit(e) {
        e.preventDefault();

        // Destrukturyzacja przed wysłaniem
        const { email: userEmail, password: userPassword } = formData;

        try {
            const response = await fetch("/api/login", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ userEmail, userPassword })
            });

            const { token, user } = await response.json(); // destrukturyzacja response!
            console.log("Zalogowano:", user.name);
        } catch (err) {
            console.error("Błąd logowania:", err);
        }
    }

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="email"
                name="email"
                value={email}
                onChange={handleChange}
                placeholder="Email"
            />
            <input
                type="password"
                name="password"
                value={password}
                onChange={handleChange}
                placeholder="Hasło"
            />
            <label>
                <input
                    type="checkbox"
                    name="rememberMe"
                    checked={rememberMe}
                    onChange={handleChange}
                />
                Zapamiętaj mnie
            </label>
            <button type="submit">Zaloguj się</button>
        </form>
    );
}
```

### 5.8. Destrukturyzacja w React Router

```javascript
import { useParams, useLocation, useNavigate } from "react-router-dom";

function ProductDetail() {
    // Destrukturyzacja URL params
    const { productId } = useParams();

    // Destrukturyzacja location
    const { pathname, search } = useLocation();

    // Destrukturyzacja navigate
    const navigate = useNavigate();

    function goBack() {
        navigate(-1);
    }

    return (
        <div>
            <h1>Produkt ID: {productId}</h1>
            <p>Ścieżka: {pathname}</p>
            <button onClick={goBack}>Wróć</button>
        </div>
    );
}
```

---

## 6. Zaawansowane techniki

### 6.1. Łączenie destrukturyzacji z innymi metodami

```javascript
const user = {
    name: "Maria",
    age: 25,
    skills: ["JavaScript", "React", "Node.js"]
};

// Destrukturyzacja + array destructuring
const { name, skills: [mainSkill, ...otherSkills] } = user;

console.log(name);       // "Maria"
console.log(mainSkill);  // "JavaScript"
console.log(otherSkills);// ["React", "Node.js"]
```

### 6.2. Destrukturyzacja w warunkach if

```javascript
const userData = { isAdmin: true, userName: "admin" };

if (userData.isAdmin) {
    console.log("Admin"); // starszy sposób
}

// Lepiej:
const { isAdmin, userName } = userData;
if (isAdmin) {
    console.log(`Admin: ${userName}`);
}

// Lub nawet bardziej kompaktowo:
if (userData.isAdmin) {
    const { userName } = userData;
    console.log(`Admin: ${userName}`);
}
```

### 6.3. Destrukturyzacja z computed properties

```javascript
const keyName = "email";
const user = { name: "Jan", email: "jan@example.com" };

// Aby wyodrębnić właściwość z dynamiczną nazwą, musisz ją najpierw pobrać
const { [keyName]: emailValue } = user;
console.log(emailValue); // "jan@example.com"
```

---

## 7. Typowe błędy i pułapki

### 7.1. Zapomniany `=` lub `:`

```javascript
// ❌ Błąd
const { name, email } user;

// ✅ Poprawnie
const { name, email } = user;
```

### 7.2. Próba destrukturyzacji niezdefiniowanego obiektu

```javascript
// ❌ Błąd
const { name, email } = undefined;

// ✅ Poprawnie – z wartością domyślną
const { name, email } = user || {};
const { name = "Anonimowy", email = "none@example.com" } = user || {};
```

### 7.3. Destrukturyzacja w złej kolejności (ważne w tablicach)

```javascript
const [first, second] = [10, 20, 30];
console.log(first);  // 10
console.log(second); // 20
// Trzeci element [30] jest zignorowany – to OK

const [a, b] = [1]; // b będzie undefined
```

---

## 8. Podsumowanie – co zapamiętać

- **Object Destructuring**: `const { prop1, prop2 } = object;`
  - Upraszcza dostęp do właściwości obiektów.
  - Zwiększa czytelność kodu.
  - Można używać aliasów i wartości domyślnych.

- **Array Destructuring**: `const [first, second] = array;`
  - Stosuje się do tablic.
  - Można pomijać elementy.
  - Wspiera rest operator (`...`).

- **W React**:
  - Destrukturyzuj `props` w parametrach komponentów.
  - Używaj do rozpakowania `state` z `useState`.
  - Używaj z `useContext`, `useParams`, event objects.
  - Destrukturyzuj API responses dla lepszej czytelności.

- **Rest operator `...`**: zbiera pozostałe właściwości/elementy w jedno.

- **Wartości domyślne**: `{ prop = defaultValue }`

---

## 9. Zadania do samodzielnego ćwiczenia

### Zadanie 1: Podstawowa destrukturyzacja

Mając obiekt:

```javascript
const book = {
    title: "Clean Code",
    author: "Robert C. Martin",
    year: 2008,
    pages: 464
};
```

Destrukturyzuj `title` i `author`, a pozostałe dane trzymaj w zmiennej `rest`.

### Zadanie 2: Destrukturyzacja parametrów funkcji

Napisz funkcję `printRecipe`, która jako parametr przyjmuje obiekt z właściwościami `name`, `servings` (domyślnie 4) i `ingredients` (tablica). Funkcja powinna wypisać te dane.

### Zadanie 3: React komponent

Stwórz komponent `ProductCard` przyjmujący props: `id`, `title`, `price`, `inStock` (domyślnie true), oraz `onBuy` (funkcja). Destrukturyzuj `props` i renderuj karę produktu.

### Zadanie 4: Zagnieżdżona destrukturyzacja

Mając taki obiekt:

```javascript
const company = {
    name: "TechCorp",
    address: {
        street: "Puławskiego 1",
        city: "Warszawa"
    },
    employees: ["Anna", "Jan", "Maria"]
};
```

Destrukturyzuj `name`, `city` (z address) i pierwszy element `employees` (przypisz mu zmienną `manager`).

### Zadanie 5: Destrukturyzacja w useEffect

Napisz `useEffect`, który pobiera dane z `https://jsonplaceholder.typicode.com/users/1` i destrukturyzuje `name`, `email`, `phone` z odpowiedzi. Wyświetl te dane w komponencie.

---

Eksperymentuj, zabawiaj się destrukturyzacją – z czasem stanie się dla Ciebie drugą naturą! 🚀

