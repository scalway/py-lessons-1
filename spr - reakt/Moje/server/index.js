import express from 'express'
import cors from 'cors'

const app = express()
app.use(cors())

app.get('/', (req, res) => {
  res.send('Hello World')
})

app.get('/task', (req, res) => {
  res.json([{
            "key": "Complete the assignment",
            "dueDate": "2024-07-01"
        },
        {
            "key": "Compl",
            "dueDate": "2024-07-01"
        }])
})

app.listen(3002, () => {
  console.log('Server is running on http://127.0.0.1:3002')
})