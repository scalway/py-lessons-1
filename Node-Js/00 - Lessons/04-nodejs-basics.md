# Node.js - Podstawy i narzędzia

Node.js to środowisko uruchomieniowe JavaScript poza przeglądarką. Pozwala na tworzenie aplikacji serwerowych, narzędzi CLI i wiele więcej.

## 1. Instalacja i podstawy

### Sprawdzenie wersji

```bash
# Sprawdź wersję Node.js
node --version  # lub node -v

# Sprawdź wersję npm
npm --version   # lub npm -v

# Sprawdź wersję npx
npx --version   # lub npx -v
```

### Uruchamianie kodu

```bash
# Uruchom plik JavaScript
node app.js

# Uruchom kod bezpośrednio (REPL)
node
> console.log("Hello World!")
> .exit

# Uruchom kod inline
node -e "console.log('Hello from command line!')"

# Sprawdź pomoc
node --help
```

## 2. NPM - Node Package Manager

### Podstawowe komendy

```bash
# Inicjalizacja nowego projektu
npm init
npm init -y  # szybka inicjalizacja z domyślnymi wartościami

# Instalacja paczek
npm install lodash              # lokalnie w projekcie
npm install -g nodemon         # globalnie
npm install --save-dev jest    # jako dev dependency

# Skróty
npm i lodash                   # skrót od install
npm i -D jest                  # skrót od --save-dev
npm i -g typescript            # skrót od --global

# Aktualizacja paczek
npm update
npm update lodash

# Usuwanie paczek
npm uninstall lodash
npm uninstall -g nodemon

# Lista zainstalowanych paczek
npm list
npm list -g --depth=0         # globalne paczki

# Informacje o paczce
npm info lodash
npm view lodash version

# Uruchamianie skryptów
npm run start
npm run dev
npm run test
npm run build
```

### Przykład package.json

```json
{
  "name": "moj-projekt",
  "version": "1.0.0",
  "description": "Przykład projektu Node.js",
  "main": "index.js",
  "type": "module",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon index.js",
    "test": "jest",
    "build": "tsc",
    "lint": "eslint .",
    "format": "prettier --write ."
  },
  "keywords": ["nodejs", "javascript", "example"],
  "author": "Jan Kowalski",
  "license": "MIT",
  "dependencies": {
    "express": "^4.18.2",
    "lodash": "^4.17.21"
  },
  "devDependencies": {
    "nodemon": "^3.0.1",
    "jest": "^29.7.0",
    "@types/node": "^20.8.0"
  },
  "engines": {
    "node": ">=18.0.0",
    "npm": ">=9.0.0"
  }
}
```

## 3. NPX - Node Package Executor

NPX pozwala uruchamiać paczki bez instalowania ich globalnie.

```bash
# Uruchom paczki bez instalacji
npx create-react-app my-app
npx typescript --init
npx prettier --write .

# Uruchom konkretną wersję paczki
npx node@18 --version

# Uruchom lokalnie zainstalowaną paczę
npx jest
npx eslint .

# Sprawdź czy paczka istnieje lokalnie, potem globalnie, na końcu pobierz
npx cowsay "Hello World!"

# Wymuś pobranie najnowszej wersji
npx --yes create-next-app@latest my-next-app

# Uruchom z GitHub
npx github:user/repo
```

### Praktyczne przykłady NPX

```bash
# Szybkie narzędzia developerskie
npx http-server                    # serwer HTTP
npx live-server                    # serwer z live reload
npx json-server --watch db.json    # mock REST API

# Generatory projektów
npx create-react-app my-react-app
npx create-next-app my-next-app
npx create-vue my-vue-app
npx @angular/cli new my-angular-app

# Narzędzia do analizy
npx bundlephobia lodash            # rozmiar paczki
npx npm-check-updates              # sprawdź aktualizacje
npx depcheck                       # nieużywane dependencje

# Utilities
npx rimraf node_modules            # usuń folder (cross-platform)
npx cross-env NODE_ENV=production node app.js
```

## 4. CommonJS - require() (tradycyjny system modułów)

### Eksportowanie modułów

```javascript
// math.js - różne sposoby eksportu
const pi = 3.14159;

function add(a, b) {
    return a + b;
}

function multiply(a, b) {
    return a * b;
}

class Calculator {
    constructor() {
        this.history = [];
    }
    
    add(a, b) {
        const result = a + b;
        this.history.push(`${a} + ${b} = ${result}`);
        return result;
    }
}

// Sposób 1: exports.property
exports.pi = pi;
exports.add = add;

// Sposób 2: module.exports (zastępuje cały export)
module.exports = {
    pi,
    add,
    multiply,
    Calculator
};

// Sposób 3: module.exports dla pojedynczej funkcji
// module.exports = add;

// Sposób 4: dodawanie do istniejącego exports
module.exports.subtract = function(a, b) {
    return a - b;
};
```

### Importowanie modułów

```javascript
// app.js - różne sposoby importu
const fs = require('fs');                    // wbudowany moduł
const path = require('path');                // wbudowany moduł
const express = require('express');          // paczka z npm

// Importy z własnych modułów
const math = require('./math');              // cały moduł
const { add, multiply } = require('./math'); // destrukturyzacja
const Calculator = require('./math').Calculator;

// Aliasy
const _ = require('lodash');
const chalk = require('chalk');

// Używanie
console.log(math.pi);                        // 3.14159
console.log(add(5, 3));                     // 8
console.log(math.multiply(4, 7));           // 28

const calc = new math.Calculator();
console.log(calc.add(10, 20));              // 30

// Przykład z fs
const content = fs.readFileSync('package.json', 'utf8');
console.log(JSON.parse(content).name);

// Asynchroniczny fs
fs.readFile('package.json', 'utf8', (err, data) => {
    if (err) throw err;
    console.log(JSON.parse(data).version);
});
```

### Wzorce CommonJS

```javascript
// utils.js - dobre praktyki CommonJS
'use strict';

const EventEmitter = require('events');
const fs = require('fs').promises; // promises API

// Prywatne funkcje (nie eksportowane)
function validateInput(data) {
    if (typeof data !== 'string') {
        throw new TypeError('Input must be a string');
    }
}

// Factory pattern
function createLogger(prefix = 'LOG') {
    return {
        info: (message) => console.log(`[${prefix}] INFO: ${message}`),
        error: (message) => console.error(`[${prefix}] ERROR: ${message}`)
    };
}

// Klasa z dziedziczeniem EventEmitter
class DataProcessor extends EventEmitter {
    constructor() {
        super();
        this.data = [];
    }
    
    async loadData(filepath) {
        try {
            const content = await fs.readFile(filepath, 'utf8');
            this.data = JSON.parse(content);
            this.emit('dataLoaded', this.data.length);
            return this.data;
        } catch (error) {
            this.emit('error', error);
            throw error;
        }
    }
}

module.exports = {
    createLogger,
    DataProcessor,
    version: '1.0.0'
};
```

## 5. ES Modules (ESM) - import/export (nowoczesny standard)

Aby używać ESM w Node.js, dodaj `"type": "module"` do `package.json` lub użyj rozszerzenia `.mjs`.

### Eksportowanie ES Modules

```javascript
// mathESM.js - różne sposoby eksportu ESM
export const PI = 3.14159;

// Named exports
export function add(a, b) {
    return a + b;
}

export function multiply(a, b) {
    return a * b;
}

export class Calculator {
    constructor() {
        this.history = [];
    }
    
    calculate(operation, a, b) {
        let result;
        switch (operation) {
            case 'add':
                result = a + b;
                break;
            case 'multiply':
                result = a * b;
                break;
            default:
                throw new Error(`Unknown operation: ${operation}`);
        }
        
        this.history.push(`${a} ${operation} ${b} = ${result}`);
        return result;
    }
    
    getHistory() {
        return [...this.history]; // shallow copy
    }
}

// Default export
export default function subtract(a, b) {
    return a - b;
}

// Re-export z innego modułu
export { readFile, writeFile } from 'fs/promises';

// Eksport z aliasem
const VERSION = '2.0.0';
export { VERSION as version };
```

### Importowanie ES Modules

```javascript
// appESM.js - różne sposoby importu ESM
import fs from 'fs/promises';                    // default import
import path from 'path';                         // default import
import express from 'express';                   // default import

// Named imports
import { PI, add, multiply, Calculator } from './mathESM.js';

// Default import z aliasem
import subtract from './mathESM.js';

// Mixed import (default + named)
import subtract, { PI, add } from './mathESM.js';

// Wszystko jako namespace
import * as math from './mathESM.js';

// Import z aliasem
import { Calculator as Calc } from './mathESM.js';

// Dynamic import (asynchroniczny)
const dynamicModule = await import('./mathESM.js');

// Conditional import
if (process.env.NODE_ENV === 'development') {
    const devTools = await import('./devTools.js');
    devTools.enableDebugMode();
}

// Używanie
console.log(PI);                                 // 3.14159
console.log(add(5, 3));                         // 8
console.log(subtract(10, 4));                   // 6

const calculator = new Calculator();
console.log(calculator.calculate('add', 15, 25)); // 40

// Namespace usage
console.log(math.PI);
console.log(math.add(1, 2));
const calc2 = new math.Calculator();
```

### Top-level await w ESM

```javascript
// dataLoader.js - top-level await
import fs from 'fs/promises';

// Można używać await na najwyższym poziomie w ESM
try {
    const packageData = await fs.readFile('package.json', 'utf8');
    const packageInfo = JSON.parse(packageData);
    
    console.log(`App: ${packageInfo.name} v${packageInfo.version}`);
    
    // Export z async data
    export const appInfo = {
        name: packageInfo.name,
        version: packageInfo.version,
        dependencies: Object.keys(packageInfo.dependencies || {})
    };
} catch (error) {
    console.error('Failed to load package info:', error.message);
    export const appInfo = { name: 'unknown', version: '0.0.0', dependencies: [] };
}
```

## 6. Porównanie CommonJS vs ESM

| Właściwość | CommonJS | ES Modules |
|------------|----------|------------|
| **Składnia** | `require()`/`module.exports` | `import`/`export` |
| **Loading** | Synchroniczny | Asynchroniczny |
| **Hoisting** | Nie | Tak (import hoisting) |
| **Conditional imports** | Łatwe | Trudniejsze (dynamic import) |
| **Tree shaking** | Ograniczone | Pełne wsparcie |
| **Top-level await** | Nie | Tak |
| **Compatibility** | Node.js natywnie | Node.js 14+, przeglądarki |
| **File extension** | `.js`, `.cjs` | `.js` (z "type": "module"), `.mjs` |

### Przykład migracji CommonJS → ESM

```javascript
// Przed (CommonJS)
const fs = require('fs');
const path = require('path');
const { promisify } = require('util');
const readFileAsync = promisify(fs.readFile);

function createConfig(options = {}) {
    return {
        port: options.port || 3000,
        host: options.host || 'localhost'
    };
}

module.exports = { createConfig, readFileAsync };

// Po (ESM)
import { readFile } from 'fs/promises';
import path from 'path';

export function createConfig(options = {}) {
    return {
        port: options.port || 3000,
        host: options.host || 'localhost'
    };
}

export { readFile as readFileAsync };
```

## 7. Dobre praktyki modułów

### 🎯 Ogólne zalecenia

```javascript
// ✅ Dobre praktyki

// 1. Używaj const dla importów
const express = require('express');
import express from 'express';

// 2. Grupuj importy logicznie
// Wbudowane moduły
import fs from 'fs/promises';
import path from 'path';

// Zewnętrzne paczki
import express from 'express';
import lodash from 'lodash';

// Własne moduły
import { config } from './config.js';
import { database } from './db/connection.js';

// 3. Używaj destrukturyzacji rozsądnie
import { readFile, writeFile } from 'fs/promises'; // ✅ OK
const { join, resolve, dirname } = require('path'); // ✅ OK

// 4. Eksportuj jawnie
export { userService, authMiddleware }; // ✅ Jasne co eksportujesz

// 5. Unikaj deep imports
import userService from './services/user/userService.js'; // ✅
// import userService from './services/user/src/lib/userService.js'; // ❌
```

### ❌ Czego unikać

```javascript
// ❌ Złe praktyki

// 1. Mixing CommonJS i ESM w tym samym projekcie bez powodu
// require() w ESM module - nie działa
// import w CommonJS - nie działa natywnie

// 2. Circular dependencies
// fileA.js imports fileB.js
// fileB.js imports fileA.js

// 3. Side effects w importach
// Unikaj kodu wykonującego się podczas importu
console.log('This runs when imported!'); // ❌

// 4. Dynamic require/import bez error handling
try {
    const module = await import('./mayNotExist.js');
} catch (error) {
    console.error('Module not found:', error.message);
}

// 5. Importy w środku funkcji (CommonJS)
function badExample() {
    const fs = require('fs'); // ❌ powinno być na górze
}
```

## 8. Alternatywni runnery

### Deno

Deno to nowoczesny runtime JavaScript/TypeScript stworzony przez twórcę Node.js.

```bash
# Instalacja Deno
curl -fsSL https://deno.land/install.sh | sh

# Sprawdź wersję
deno --version

# Uruchom plik
deno run app.ts

# Uruchom z pozwoleniami
deno run --allow-net --allow-read server.ts

# Uruchom z URL
deno run https://deno.land/std@0.200.0/examples/welcome.ts
```

```javascript
// server.ts - Deno example
import { serve } from "https://deno.land/std@0.200.0/http/server.ts";

const port = 8000;

const handler = (request: Request): Response => {
  const body = `Your user-agent is:\n\n${request.headers.get("user-agent") ?? "Unknown"}`;
  
  return new Response(body, { 
    status: 200,
    headers: { "content-type": "text/plain" }
  });
};

console.log(`HTTP server running. Access it at: http://localhost:${port}/`);
await serve(handler, { port });
```

```typescript
// fileUtils.ts - Deno utilities
import { ensureDir } from "https://deno.land/std@0.200.0/fs/mod.ts";

export async function createProject(name: string) {
  const projectPath = `./${name}`;
  
  // Ensure directory exists
  await ensureDir(projectPath);
  
  // Create package.json equivalent (deno.json)
  const config = {
    name,
    version: "1.0.0",
    tasks: {
      start: "deno run --allow-net main.ts",
      dev: "deno run --allow-net --watch main.ts"
    },
    imports: {
      "std/": "https://deno.land/std@0.200.0/"
    }
  };
  
  await Deno.writeTextFile(
    `${projectPath}/deno.json`, 
    JSON.stringify(config, null, 2)
  );
  
  console.log(`✅ Project ${name} created successfully!`);
}

// Usage
if (import.meta.main) {
  await createProject("my-deno-app");
}
```

### Bun

Bun to bardzo szybki runtime JavaScript z wbudowanym bundlerem i package managerem.

```bash
# Instalacja Bun
curl -fsSL https://bun.sh/install | bash

# Sprawdź wersję
bun --version

# Uruchom plik
bun run app.js

# Instaluj paczki (bardzo szybkie!)
bun install
bun add express
bun add -d typescript

# Uruchom TypeScript bezpośrednio
bun run app.ts
```

```javascript
// server.js - Bun example
import { serve } from "bun";

const server = serve({
  port: 3000,
  fetch(request) {
    const url = new URL(request.url);
    
    if (url.pathname === "/") {
      return new Response("Hello from Bun! 🥖", {
        headers: { "Content-Type": "text/plain" }
      });
    }
    
    if (url.pathname === "/json") {
      return Response.json({ 
        message: "Fast JSON response",
        timestamp: Date.now(),
        runtime: "Bun"
      });
    }
    
    return new Response("Not Found", { status: 404 });
  },
});

console.log(`🚀 Server running on http://localhost:${server.port}`);
```

```typescript
// bunUtils.ts - Bun specific features
import { write, file } from "bun";

// Ultra fast file operations
export async function processFiles(directory: string) {
  const files = await Array.fromAsync(
    new Bun.Glob("**/*.{js,ts}").scan(directory)
  );
  
  console.log(`Found ${files.length} JavaScript/TypeScript files`);
  
  for (const filePath of files) {
    const fileObj = file(filePath);
    const content = await fileObj.text();
    const lines = content.split('\n').length;
    
    console.log(`📁 ${filePath}: ${lines} lines`);
  }
}

// Bun's built-in test runner
import { expect, test } from "bun:test";

test("fast math", () => {
  expect(2 + 2).toBe(4);
});

// Hot reloading in development
if (process.env.NODE_ENV === "development") {
  console.log("🔥 Hot reloading enabled in Bun!");
}
```

### Porównanie runtimes

| Właściwość | Node.js | Deno | Bun |
|------------|---------|------|-----|
| **Wydajność** | Dobra | Dobra | Bardzo wysoka |
| **TypeScript** | Wymaga transpilacji | Natywne wsparcie | Natywne wsparcie |
| **Package manager** | npm/yarn | Wbudowany | Wbudowany (szybki) |
| **Bezpieczeństwo** | Brak ograniczeń | Sandbox domyślnie | Brak ograniczeń |
| **Ekosystem** | Największy | Rosnący | Młody |
| **Web APIs** | Ograniczone | Fetch, streams itp. | Fetch, WebSocket itp. |
| **Backward compatibility** | Wysoka | Ograniczona | Wysoka z Node.js |

## 9. Podsumowanie

### 🎯 Zalecenia wyboru:

**Node.js** - gdy:
- Potrzebujesz stabilności i dużego ekosystemu
- Pracujesz z istniejącymi projektami
- Używasz wielu paczek npm

**Deno** - gdy:
- Chcesz TypeScript z pudełka
- Bezpieczeństwo jest priorytetem
- Preferujesz web standardy

**Bun** - gdy:
- Wydajność jest kluczowa
- Chcesz szybkich install/bundling
- Eksperymentujesz z nowymi technologiami

### 📋 Dobre praktyki:

1. **Używaj ESM** w nowych projektach
2. **Grupuj importy** logicznie
3. **Unikaj circular dependencies**
4. **Używaj type safety** (TypeScript)
5. **Testuj różne runtimes** dla konkretnych use cases
6. **Monitoruj performance** w produkcji

**Wniosek:** Każdy runtime ma swoje miejsce. Node.js dla stabilności, Deno dla nowoczesności i bezpieczeństwa, Bun dla wydajności.