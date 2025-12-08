const express = require('express')
const app = express()
const port = 3002
const path = require('node:path')

app.use(express.static('strony'))
app.use(express.static('files'))
//npm instal - to pobiera nam node moguels - JEST TO POTRZEBNE
//
//link do otwarcia http://localhost:3002/

app.get('/', (req, res) => {
  res.sendFile('index.html', {root: `${__dirname}/strony`})
})

app.get('/podstrona', (req, res) => {
  res.sendFile('podstrona.html', {root: `${__dirname}/strony`})
})

app.get('/podstrona2', (req, res) => {
  res.sendFile('podstrona2.html', {root: `${__dirname}/strony`});
  })

app.get('/css', (req, res) => {
  res.sendFile('style.css', {root:`${__dirname}/strony`})
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})