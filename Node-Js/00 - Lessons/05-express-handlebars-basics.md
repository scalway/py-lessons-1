# Express.js i Handlebars.js - Podstawy

Express.js to minimalistyczny framework webowy dla Node.js, a Handlebars.js to engine do templatingu HTML. Razem tworzą potężną kombinację do budowy aplikacji webowych.

## 1. Express.js - Podstawy

### Instalacja i setup

```bash
# Inicjalizacja projektu
npm init -y

# Instalacja Express
npm install express

# Instalacja nodemon dla developmentu
npm install -D nodemon

# Dodaj do package.json
"scripts": {
  "start": "node app.js",
  "dev": "nodemon app.js"
}
```

### Podstawowa aplikacja Express

```javascript
// app.js
const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
app.use(express.json()); // parsowanie JSON
app.use(express.urlencoded({ extended: true })); // parsowanie form data
app.use(express.static('public')); // serwowanie plików statycznych

// Podstawowe routy
app.get('/', (req, res) => {
    res.send('<h1>Witaj w Express!</h1>');
});

app.get('/api/users', (req, res) => {
    res.json([
        { id: 1, name: 'Jan', email: 'jan@example.com' },
        { id: 2, name: 'Anna', email: 'anna@example.com' }
    ]);
});

// Start serwera
app.listen(PORT, () => {
    console.log(`🚀 Serwer działa na porcie ${PORT}`);
});
```

### Express Routing

```javascript
// routes.js
const express = require('express');
const router = express.Router();

// GET route z parametrami
router.get('/users/:id', (req, res) => {
    const userId = req.params.id;
    const user = { id: userId, name: 'Przykładowy User' };
    res.json(user);
});

// POST route
router.post('/users', (req, res) => {
    const { name, email } = req.body;
    
    if (!name || !email) {
        return res.status(400).json({ 
            error: 'Wymagane pola: name, email' 
        });
    }
    
    const newUser = { id: Date.now(), name, email };
    res.status(201).json(newUser);
});

// PUT route
router.put('/users/:id', (req, res) => {
    const { id } = req.params;
    const { name, email } = req.body;
    
    const updatedUser = { id: parseInt(id), name, email };
    res.json(updatedUser);
});

// DELETE route
router.delete('/users/:id', (req, res) => {
    const { id } = req.params;
    res.json({ message: `Użytkownik ${id} został usunięty` });
});

module.exports = router;
```

```javascript
// app.js z routami
const express = require('express');
const userRoutes = require('./routes');

const app = express();

app.use(express.json());
app.use('/api', userRoutes); // prefix dla wszystkich routów

app.listen(3000, () => {
    console.log('Serwer działa na porcie 3000');
});
```

### Middleware w Express

```javascript
// middleware.js
const express = require('express');
const app = express();

// Middleware logowania
const logger = (req, res, next) => {
    console.log(`${new Date().toISOString()} - ${req.method} ${req.path}`);
    next(); // ważne! wywołaj next() aby przejść dalej
};

// Middleware autoryzacji
const requireAuth = (req, res, next) => {
    const token = req.headers.authorization;
    
    if (!token) {
        return res.status(401).json({ error: 'Brak tokenu autoryzacji' });
    }
    
    // Symulacja weryfikacji tokenu
    if (token !== 'Bearer secret-token') {
        return res.status(403).json({ error: 'Nieprawidłowy token' });
    }
    
    req.user = { id: 1, name: 'Admin' }; // dodaj user do request
    next();
};

// Middleware obsługi błędów
const errorHandler = (err, req, res, next) => {
    console.error('❌ Błąd:', err.message);
    
    res.status(500).json({
        error: 'Wewnętrzny błąd serwera',
        message: err.message
    });
};

// Użycie middleware
app.use(logger); // globalny middleware

app.get('/public', (req, res) => {
    res.json({ message: 'Publiczny endpoint' });
});

app.get('/private', requireAuth, (req, res) => {
    res.json({ 
        message: 'Prywatny endpoint',
        user: req.user 
    });
});

app.use(errorHandler); // middleware błędów na końcu

app.listen(3000);
```

## 2. Handlebars.js - Engine templatingu

### Instalacja i konfiguracja

```bash
# Instalacja Handlebars dla Express
npm install express-handlebars
```

```javascript
// app.js z Handlebars
const express = require('express');
const { engine } = require('express-handlebars');

const app = express();

// Konfiguracja Handlebars
app.engine('handlebars', engine({
    defaultLayout: 'main', // główny layout
    layoutsDir: 'views/layouts/', // folder z layoutami
    partialsDir: 'views/partials/' // folder z partialami
}));

app.set('view engine', 'handlebars');
app.set('views', './views');

// Middleware
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));

// Routes z renderowaniem
app.get('/', (req, res) => {
    const data = {
        title: 'Strona główna',
        message: 'Witaj w aplikacji Express + Handlebars!',
        users: [
            { name: 'Jan', age: 25 },
            { name: 'Anna', age: 30 },
            { name: 'Piotr', age: 22 }
        ]
    };
    
    res.render('home', data);
});

app.listen(3000, () => {
    console.log('Serwer na porcie 3000');
});
```

### Struktura folderów Handlebars

```
views/
├── layouts/
│   └── main.handlebars     # główny layout
├── partials/
│   ├── header.handlebars   # header
│   ├── footer.handlebars   # footer
│   └── user-card.handlebars # komponent użytkownika
├── home.handlebars         # strona główna
├── users.handlebars        # lista użytkowników
└── user-detail.handlebars  # szczegóły użytkownika
```

### Główny layout

```handlebars
<!-- views/layouts/main.handlebars -->
<!DOCTYPE html>
<html lang="pl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title}} - Moja Aplikacja</title>
    <link rel="stylesheet" href="/css/style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    {{> header}}
    
    <main class="container mt-4">
        {{{body}}} <!-- tutaj wstawi się zawartość strony -->
    </main>
    
    {{> footer}}
    
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js"></script>
    <script src="/js/main.js"></script>
</body>
</html>
```

### Partials (komponenty wielokrotnego użytku)

```handlebars
<!-- views/partials/header.handlebars -->
<header class="bg-primary text-white">
    <nav class="navbar navbar-expand-lg navbar-dark">
        <div class="container">
            <a class="navbar-brand" href="/">Moja App</a>
            <div class="navbar-nav">
                <a class="nav-link" href="/">Home</a>
                <a class="nav-link" href="/users">Użytkownicy</a>
                <a class="nav-link" href="/about">O nas</a>
            </div>
        </div>
    </nav>
</header>
```

```handlebars
<!-- views/partials/footer.handlebars -->
<footer class="bg-dark text-white text-center py-3 mt-5">
    <div class="container">
        <p>&copy; 2024 Moja Aplikacja. Wszystkie prawa zastrzeżone.</p>
    </div>
</footer>
```

```handlebars
<!-- views/partials/user-card.handlebars -->
<div class="card mb-3">
    <div class="card-body">
        <h5 class="card-title">{{name}}</h5>
        <p class="card-text">
            <strong>Email:</strong> {{email}}<br>
            <strong>Wiek:</strong> {{age}} lat
        </p>
        {{#if active}}
            <span class="badge bg-success">Aktywny</span>
        {{else}}
            <span class="badge bg-secondary">Nieaktywny</span>
        {{/if}}
        
        <div class="mt-2">
            <a href="/users/{{id}}" class="btn btn-primary btn-sm">Szczegóły</a>
            <a href="/users/{{id}}/edit" class="btn btn-warning btn-sm">Edytuj</a>
        </div>
    </div>
</div>
```

### Przykładowe views

```handlebars
<!-- views/home.handlebars -->
<div class="row">
    <div class="col-md-8">
        <h1>{{title}}</h1>
        <p class="lead">{{message}}</p>
        
        {{#if users}}
            <h3>Ostatnio zarejestrowani użytkownicy:</h3>
            <div class="row">
                {{#each users}}
                    <div class="col-md-4">
                        {{> user-card}}
                    </div>
                {{/each}}
            </div>
        {{else}}
            <p>Brak użytkowników do wyświetlenia.</p>
        {{/if}}
    </div>
    
    <div class="col-md-4">
        <div class="card">
            <div class="card-header">
                <h5>Szybkie akcje</h5>
            </div>
            <div class="card-body">
                <a href="/users/new" class="btn btn-success mb-2 d-block">Dodaj użytkownika</a>
                <a href="/users" class="btn btn-info d-block">Zobacz wszystkich</a>
            </div>
        </div>
    </div>
</div>
```

### Handlebars helpers i warunki

```handlebars
<!-- views/users.handlebars -->
<h1>Lista użytkowników ({{users.length}})</h1>

{{#if users.length}}
    <div class="row mb-3">
        <div class="col">
            <a href="/users/new" class="btn btn-success">Dodaj nowego</a>
        </div>
    </div>
    
    {{#each users}}
        <div class="user-item {{#if @first}}first{{/if}} {{#if @last}}last{{/if}}">
            <h3>{{@index}}. {{name}}</h3>
            <p>Email: {{email}}</p>
            
            {{!-- Warunki --}}
            {{#if age}}
                {{#if (gt age 18)}}
                    <span class="badge bg-success">Pełnoletni ({{age}} lat)</span>
                {{else}}
                    <span class="badge bg-warning">Niepełnoletni ({{age}} lat)</span>
                {{/if}}
            {{/if}}
            
            {{!-- Iteracja po hobby --}}
            {{#if hobbies}}
                <p>Hobby: 
                    {{#each hobbies}}
                        <span class="badge bg-info">{{this}}</span>{{#unless @last}}, {{/unless}}
                    {{/each}}
                </p>
            {{/if}}
        </div>
        
        {{#unless @last}}<hr>{{/unless}}
    {{/each}}
{{else}}
    <div class="alert alert-info">
        <h4>Brak użytkowników</h4>
        <p>Nie ma jeszcze żadnych użytkowników w systemie.</p>
        <a href="/users/new" class="btn btn-primary">Dodaj pierwszego</a>
    </div>
{{/if}}
```

### Formularz z Handlebars

```handlebars
<!-- views/user-form.handlebars -->
<h1>{{#if user}}Edytuj{{else}}Dodaj{{/if}} użytkownika</h1>

<form action="{{#if user}}/users/{{user.id}}{{else}}/users{{/if}}" method="POST">
    {{#if user}}
        <input type="hidden" name="_method" value="PUT">
    {{/if}}
    
    <div class="mb-3">
        <label for="name" class="form-label">Imię *</label>
        <input type="text" class="form-control" id="name" name="name" 
               value="{{user.name}}" required>
    </div>
    
    <div class="mb-3">
        <label for="email" class="form-label">Email *</label>
        <input type="email" class="form-control" id="email" name="email" 
               value="{{user.email}}" required>
    </div>
    
    <div class="mb-3">
        <label for="age" class="form-label">Wiek</label>
        <input type="number" class="form-control" id="age" name="age" 
               value="{{user.age}}" min="1" max="120">
    </div>
    
    <div class="mb-3">
        <div class="form-check">
            <input type="checkbox" class="form-check-input" id="active" name="active" 
                   {{#if user.active}}checked{{/if}}>
            <label class="form-check-label" for="active">
                Konto aktywne
            </label>
        </div>
    </div>
    
    <button type="submit" class="btn btn-primary">
        {{#if user}}Zaktualizuj{{else}}Dodaj{{/if}}
    </button>
    <a href="/users" class="btn btn-secondary">Anuluj</a>
</form>
```

## 3. Kompletny przykład aplikacji

```javascript
// app.js - kompletna aplikacja
const express = require('express');
const { engine } = require('express-handlebars');

const app = express();

// Konfiguracja Handlebars
app.engine('handlebars', engine({
    defaultLayout: 'main',
    helpers: {
        // Custom helper
        formatDate: (date) => {
            return new Date(date).toLocaleDateString('pl-PL');
        },
        eq: (a, b) => a === b,
        gt: (a, b) => a > b
    }
}));

app.set('view engine', 'handlebars');

// Middleware
app.use(express.static('public'));
app.use(express.urlencoded({ extended: true }));
app.use(express.json());

// Mock database
let users = [
    { id: 1, name: 'Jan Kowalski', email: 'jan@example.com', age: 25, active: true },
    { id: 2, name: 'Anna Nowak', email: 'anna@example.com', age: 30, active: true },
    { id: 3, name: 'Piotr Wiśniewski', email: 'piotr@example.com', age: 22, active: false }
];

// Routes
app.get('/', (req, res) => {
    res.render('home', {
        title: 'Strona główna',
        message: 'Witaj w aplikacji Express + Handlebars!',
        users: users.slice(0, 3) // pokaż tylko 3 pierwszych
    });
});

app.get('/users', (req, res) => {
    res.render('users', {
        title: 'Lista użytkowników',
        users
    });
});

app.get('/users/new', (req, res) => {
    res.render('user-form', {
        title: 'Nowy użytkownik'
    });
});

app.post('/users', (req, res) => {
    const { name, email, age, active } = req.body;
    const newUser = {
        id: users.length + 1,
        name,
        email,
        age: parseInt(age),
        active: active === 'on'
    };
    
    users.push(newUser);
    res.redirect('/users');
});

app.get('/users/:id', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    
    if (!user) {
        return res.status(404).render('error', {
            title: 'Błąd 404',
            message: 'Użytkownik nie został znaleziony'
        });
    }
    
    res.render('user-detail', {
        title: `Szczegóły: ${user.name}`,
        user
    });
});

app.get('/users/:id/edit', (req, res) => {
    const user = users.find(u => u.id === parseInt(req.params.id));
    
    if (!user) {
        return res.status(404).send('Użytkownik nie znaleziony');
    }
    
    res.render('user-form', {
        title: `Edytuj: ${user.name}`,
        user
    });
});

app.post('/users/:id', (req, res) => {
    const userIndex = users.findIndex(u => u.id === parseInt(req.params.id));
    
    if (userIndex === -1) {
        return res.status(404).send('Użytkownik nie znaleziony');
    }
    
    const { name, email, age, active } = req.body;
    users[userIndex] = {
        ...users[userIndex],
        name,
        email,
        age: parseInt(age),
        active: active === 'on'
    };
    
    res.redirect('/users');
});

app.listen(3000, () => {
    console.log('🚀 Serwer działa na http://localhost:3000');
});
```

## 4. Dobre praktyki

### 🎯 Struktura projektu

```
moja-app/
├── public/           # pliki statyczne
│   ├── css/
│   ├── js/
│   └── img/
├── views/            # templates Handlebars
│   ├── layouts/
│   ├── partials/
│   └── *.handlebars
├── routes/           # pliki z routami
├── middleware/       # custom middleware
├── models/           # modele danych
├── config/           # konfiguracja
├── package.json
└── app.js
```

### ✅ Dobre praktyki Express

```javascript
// 1. Używaj router dla organizacji kodu
const userRouter = require('./routes/users');
app.use('/users', userRouter);

// 2. Middleware walidacji
const validateUser = (req, res, next) => {
    const { name, email } = req.body;
    if (!name || !email) {
        return res.status(400).json({ error: 'Wymagane pola: name, email' });
    }
    next();
};

// 3. Environment variables
const PORT = process.env.PORT || 3000;
const NODE_ENV = process.env.NODE_ENV || 'development';

// 4. Error handling
app.use((err, req, res, next) => {
    console.error(err.stack);
    res.status(500).send('Coś poszło nie tak!');
});

// 5. Security headers (helmet)
// npm install helmet
const helmet = require('helmet');
app.use(helmet());
```

### ✅ Dobre praktyki Handlebars

```handlebars
{{!-- 1. Komentarze w Handlebars --}}

{{!-- 2. Escapowanie HTML (domyślnie) --}}
<p>{{userInput}}</p> <!-- bezpieczne -->

{{!-- 3. Raw HTML tylko gdy potrzebne --}}
<div>{{{trustedHTMLContent}}}</div>

{{!-- 4. Używaj partials dla powtarzalnych elementów --}}
{{> user-card user=currentUser}}

{{!-- 5. Logiczne grupowanie w if/each --}}
{{#if users.length}}
    {{#each users}}
        {{> user-item}}
    {{/each}}
{{else}}
    <p>Brak danych</p>
{{/if}}
```

### ❌ Czego unikać

```javascript
// ❌ Brak error handling
app.get('/users/:id', (req, res) => {
    const user = database.findUser(req.params.id); // może rzucić błąd
    res.json(user);
});

// ✅ Z error handling  
app.get('/users/:id', async (req, res, next) => {
    try {
        const user = await database.findUser(req.params.id);
        if (!user) {
            return res.status(404).json({ error: 'Użytkownik nie znaleziony' });
        }
        res.json(user);
    } catch (error) {
        next(error);
    }
});

// ❌ Inline HTML w routach
app.get('/', (req, res) => {
    res.send('<h1>Hello</h1><p>World</p>'); // trudne w utrzymaniu
});

// ✅ Używaj templating engine
app.get('/', (req, res) => {
    res.render('home', { title: 'Hello', message: 'World' });
});
```

## 5. Podsumowanie

### Express.js
- **Minimalny** - tylko to co potrzebne
- **Middleware** - modularna architektura  
- **Routing** - elastyczne zarządzanie ścieżkami
- **Ecosystem** - ogromna liczba dodatków

### Handlebars.js
- **Logic-less** - czysta separacja logiki i prezentacji
- **Layouts** - DRY principle dla HTML
- **Partials** - komponenty wielokrotnego użytku
- **Helpers** - custom funkcje w templatech

### 🎯 Najważniejsze zalecenia:
1. **Organizuj kod** w foldery i moduły
2. **Używaj middleware** dla wspólnej logiki
3. **Waliduj dane** zawsze
4. **Obsługuj błędy** gracefully
5. **Separuj logikę** od prezentacji
6. **Testuj** aplikację regularnie

Express + Handlebars to solidna podstawa do tworzenia aplikacji webowych w Node.js!