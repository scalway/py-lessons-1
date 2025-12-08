const express = require('express')
const app = express()
const port = 3000
const path = require('node:path')
const { lookupService } = require('node:dns')


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

app.use(express.static('strony'))

app.listen(port,()=>{
    console.log(`Example app listening on port ${port}`)
})