let todos = []
let nextId = 1

// IMPORTANT: keep module-level storage in sync with index.js on the same instance.
// In serverless environments storage is ephemeral and may reset between invocations.

export default function handler(req, res) {
  const {
    query: { id },
    method,
    body
  } = req

  const todoId = Number(id)

  if (Number.isNaN(todoId)) {
    return res.status(400).json({ error: 'Invalid id' })
  }

  // Find index
  const idx = todos.findIndex((t) => t.id === todoId)

  if (method === 'GET') {
    if (idx === -1) return res.status(404).json({ error: 'Todo not found' })
    return res.status(200).json(todos[idx])
  }

  if (method === 'PUT') {
    if (idx === -1) return res.status(404).json({ error: 'Todo not found' })
    const { title, description, completed } = body || {}
    if (title !== undefined) todos[idx].title = String(title)
    if (description !== undefined) todos[idx].description = description
    if (completed !== undefined) todos[idx].completed = Boolean(completed)
    return res.status(200).json(todos[idx])
  }

  if (method === 'DELETE') {
    if (idx === -1) return res.status(404).json({ error: 'Todo not found' })
    todos.splice(idx, 1)
    return res.status(200).json({ message: 'Todo deleted' })
  }

  res.setHeader('Allow', ['GET', 'PUT', 'DELETE'])
  res.status(405).end(`Method ${method} Not Allowed`)
}
