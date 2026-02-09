export default function handler(req, res) {
  res.status(200).json({ message: 'Todo API (Vercel Serverless) - see /api/todos' })
}
