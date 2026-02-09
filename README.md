# Todo App

A full-stack todo application with user authentication and task management. Built with FastAPI backend and modern frontend support.

## Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLModel** - SQL + Python data models
- **SQLAlchemy** - ORM
- **Uvicorn** - ASGI server
- **Python-Jose** - JWT token handling
- **Passlib + Bcrypt** - Secure password hashing
- **Pydantic** - Data validation

### Frontend (Ready for integration)
- **Node.js** - JavaScript runtime
- **Express** - Web framework

### Database
- **SQLite** - Lightweight development database

### DevOps
- **Docker** - Containerization
- **Kubernetes** - Orchestration

## Features

✅ **User Authentication**
- Signup with username and password
- Login with JWT token generation
- Password hashing with bcrypt
- /me endpoint to get current user

✅ **Todo Management**
- Create, Read, Update, Delete (CRUD) todos
- Mark todos as completed/incomplete
- Todos belong to logged-in users only
- Ownership protection (users can't modify others' todos)
- Input validation with error handling

✅ **Security**
- JWT-based authentication
- OAuth2 password flow
- Owner-based access control
- Password encryption
- HTTPException error handling

## Project Structure

```
todo-app/
├── backend/
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py          # User model
│   │   └── todo.py          # Todo model
│   ├── services/
│   │   ├── auth_service.py  # Auth business logic
│   │   └── todo_service.py  # Todo business logic
│   ├── routes/
│   │   └── todo_routes.py   # Todo API routes (optional)
│   ├── auth.py              # Password & token utilities
│   ├── database.py          # Database configuration
│   ├── dependencies.py      # Dependency injection (get_current_user)
│   ├── schemas.py           # Pydantic schemas
│   ├── main.py              # FastAPI app & endpoints
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile           # Container image
├── frontend/                # React/Next.js app
├── k8s/                     # Kubernetes configs
├── README.md
└── app/                     # Node.js frontend
```

## Quick Start

### Prerequisites
- Python 3.8+
- pip3

### Installation & Run

```bash
# Navigate to backend
cd backend

# Install dependencies
pip3 install -r requirements.txt

# Run development server
python3 -m uvicorn main:app --reload
```

Server runs on: `http://localhost:8000`

**API Documentation**: http://localhost:8000/docs

## Core API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/signup` | Create new user |
| POST | `/login` | Get JWT token |
| GET | `/me` | Get current user |

### Todos (All require JWT token)

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/todos` | Create todo |
| GET | `/todos` | List user's todos |
| PUT | `/todos/{id}` | Update todo |
| DELETE | `/todos/{id}` | Delete todo |

## Authentication Example

```bash
# 1. Signup
curl -X POST http://localhost:8000/signup \
  -H "Content-Type: application/json" \
  -d '{"username": "john", "password": "pass123"}'

# 2. Login (get token)
curl -X POST http://localhost:8000/login \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d 'username=john&password=pass123'

# Token response:
# {"access_token": "eyJhbGc...", "token_type": "bearer"}

# 3. Use token (replace TOKEN)
TOKEN="eyJhbGc..."
curl -X GET http://localhost:8000/todos \
  -H "Authorization: Bearer $TOKEN"
```

## Todo CRUD Examples

### Create Todo
```bash
curl -X POST http://localhost:8000/todos \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer TOKEN" \
  -d '{"title": "Buy milk", "description": "Organic milk"}'
```

### Get All Todos
```bash
curl -X GET http://localhost:8000/todos \
  -H "Authorization: Bearer TOKEN"
```

### Update Todo
```bash
curl -X PUT http://localhost:8000/todos/1 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer TOKEN" \
  -d '{"completed": true}'
```

### Delete Todo
```bash
curl -X DELETE http://localhost:8000/todos/1 \
  -H "Authorization: Bearer TOKEN"
```

## Key Security Features

✅ **Ownership Protection** - Users can only see/modify their own todos
✅ **Password Hashing** - Bcrypt salt-based hashing
✅ **JWT Tokens** - 30-minute expiration, HS256 signature
✅ **Input Validation** - Pydantic validation with length checks
✅ **HTTP Error Codes** - Proper 400/401/403/404 responses

## Data Validation

**Signup/Login**:
- Username: 3-50 characters
- Password: 6+ characters

**Create Todo**:
- Title: 1-200 characters (required)
- Description: Optional, max 1000 characters

## Error Handling

| Status | Example |
|--------|---------|
| 400 | Bad request (invalid data, username exists) |
| 401 | Unauthorized (invalid token) |
| 403 | Forbidden (accessing another user's todo) |
| 404 | Not found (todo doesn't exist) |
| 422 | Validation error (invalid field) |

## Kubernetes Deployment

```bash
# Build Docker image
eval $(minikube -p minikube docker-env)
docker build -t todo-app:1.0 ./app

# Deploy
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml

# Verify
kubectl get pods
kubectl get svc
minikube service todo-service --url
```

## Troubleshooting

**Port already in use?**
```bash
python3 -m uvicorn main:app --reload --port 8001
```

**Dependencies missing?**
```bash
cd backend
pip3 install -r requirements.txt
```

**Reset database?**
```bash
rm backend/todo.db
# Restart server to recreate
```

## Project Completion Status

✅ Authentication (Signup, Login, JWT, /me)
✅ Todo CRUD operations
✅ User ownership verification
✅ Input validation with Pydantic
✅ Proper HTTP error handling
✅ Clean layered architecture
✅ Comprehensive README & API docs
✅ Security (password hashing, JWT, access control)

**Status**: 100% Complete ✓

## Future Enhancements

- Pagination support
- Filtering by completion status
- Search functionality
- Due dates for todos
- Todo categories/tags
- Real-time updates with WebSockets

## License

MIT License