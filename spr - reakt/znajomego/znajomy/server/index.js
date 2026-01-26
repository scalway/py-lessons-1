import express from 'express'
import fs from 'node:fs/promises'
import cors from 'cors'
import { writeFile } from 'node:fs'

const fileName = 'tasks.json'
const port = 3001
const app = express()
app.use(express.urlencoded())
app.use(express.json())
app.use(cors())
try {
    await fs.readFile(fileName)
    if (await fs.readFile(fileName)) {
        const data = [
            {
                id: 1,
                title: 'Pierwszy task',
                description: 'Pierwsze zadanie na serwerze'
            },
            {
                id: 2,
                title: 'Drugi task',
                description: 'Drugie zadanie na serwerze'
            }
        ]
        await fs.writeFile(fileName, JSON.stringify(data, null, 2))
    }
} catch {
    const data = [
        {
            id: 1,
            title: 'Pierwszy task',
            description: 'Pierwsze zadanie na serwerze'
        },
        {
            id: 2,
            title: 'Drugi task',
            description: 'Drugie zadanie na serwerze'
        }
    ]
    await fs.writeFile(fileName, JSON.stringify(data, null, 2))
}

app.get('/tasks', async (req, res) => {
    const result = await fs.readFile(fileName)
    const data = JSON.parse(result)
    res.json(data)
})

app.post('/add',async(req,res)=>{
    const title = req.body.title
    const description = req.body.description
    const result = await fs.readFile(fileName)
    const data = JSON.parse(result)
    const id = data[data.length-1].id + 1
    const newTask = {
        id:id,
        title:title,
        description:description
    }
    data.push(newTask)
    await fs.writeFile(fileName,JSON.stringify(data,null,2))
    res.sendStatus(200)
})
app.listen(port, console.log(`http://localhost:${port}`))