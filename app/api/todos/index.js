let todos = []
let nextId = 1

export default function handler(req, res) {
  const { method } = req

  if (method === 'GET') {
    return res.status(200).json(todos)
  }

  if (method === 'POST') {
    const { title, description } = req.body || {}

    if (!title || String(title).trim().length === 0) {
      return res.status(400).json({ error: 'Title is required' })
    }

    const todo = {
      id: nextId++,
      title: String(title).trim(),
      description: description ?? null,
      completed: false
    }

    todos.push(todo)
    return res.status(201).json(todo)
  }

  res.setHeader('Allow', ['GET', 'POST'])
  res.status(405).end(`Method ${method} Not Allowed`)
}
