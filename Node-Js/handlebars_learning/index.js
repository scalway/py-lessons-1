import express from 'express'; // to jest nowy sposob na importowanie.   to samo co komentarz nizej
import { engine } from 'express-handlebars';
import fs from 'node:fs';

//const express = require('express');     // stary sposub na impotrowanie
const app = express();
app.use(express.urlencoded({ extended: true }));


app.engine('handlebars', engine());// pieerwsze to nazwa engina. (to jest rejestracja engina)
app.set('view engine', 'handlebars');// ustawiamuy view engine na handlebars
app.set('views', './views');// ustawiamy sciezke do widokow

app.get('/', (req, res) => {
    res.render('home', {
        user_namse: 'Kuba',
        title: 'Strona główna'
    }); //nazwa pliku ktory mam opokazac
});

app.get('/podstrona', (req, res) => {
    res.render('subhandlebars',{
        title: 'Podstrona'
    }); //nazwa pliku ktory mam opokazac
});

app.get('/podstrona2', (req,res) => {
    res.render('podstrona2', {
        user_name: 'kubulcia',
        title:'podstrona 2'
    });
});

app.get('/formularz', (req,res) => {
    

    let content = "";
    let posts = [];
    try{
        content = fs.readFileSync('./wpisy.txt', 'utf-8');
    }catch(err){
        console.error(err);
    }

    if(content.length >0){
        posts = content.split('\n')
        posts = posts.map((el) => {
            return el.trim();
        });
    }

    res.render('formularz', {
        title: 'Formularz',
        arr: posts
    });

});

app.post('/formularz', (req,res) => {
    const { name, content } = req.body;

    const data = new Date()
    const entry = `\n nick: ${name}. content: ${content} date: ${data.toLocaleString()}`;

    try {
        fs.appendFileSync('./wpisy.txt', entry, 'utf-8'); // dopisz do pliku
    } catch (err) {
        console.error('Błąd zapisu:', err);
    }

    res.redirect('/formularz');
});

app.listen(5001, function (){
    console.log('Serwer działa na porcie 5001');
});



// w  PACKAGE.JSON POD "license":"ISC"  dodalem  to "type" : "moduels", sam tu dopisalem i to pokazuje jak importujemy zeczy moduels jest tym nowym typem