const express = require('express')
const { lookupService } = require('node:dns')
const app = express()
const port = 3000
const path = require('node:path')

import data from "./data.json"


const logger = ((req,res,next) => {
    let d = new Date()
    console.log(req.path, 'Time: ' + d.toDateString())
    next()
})

const lucky_number = ((req,res,next)=>{
    let num = Math.floor(Math.random()*10)+1
    if(num<=5){
        res.sendStatus(404)
    }
    else{
        next()
    }
})

app.use(logger);
app.use(lucky_number);

const datajs = data;

console.log(datajs);




app.use(express.static('stronki'))
app.listen(port,()=>{
    console.log(`Example app listening on port ${port}`)
})