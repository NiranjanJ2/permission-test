# TaskFlow API

A FastAPI-based task management system with authentication and real-time updates.

## Features

- RESTful API for task management
- User authentication with JWT
- Real-time updates via WebSockets
- PostgreSQL database with SQLAlchemy ORM
- Redis for caching and session management
- Email notifications via SendGrid
- File uploads to AWS S3
- Payment processing with Stripe
- AI-powered task suggestions via OpenAI

## Prerequisites

- Python >= 3.9
- PostgreSQL >= 14.0
- Redis >= 6.0

## Quick Start

1. Clone and setup:
```bash
git clone https://github.com/yourusername/taskflow-api.git
cd taskflow-api
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. Configure environment variables:
```bash
cp .env.example .env
# Edit .env with your credentials
```

3. Initialize the database:
```bash
alembic upgrade head
```

4. Start the development server:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure
```
taskflow-api/
├── main.py              # Application entry point
├── config.py            # Configuration management
├── database.py          # Database connection
├── models.py            # SQLAlchemy models
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not in git)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## API Endpoints

### Tasks
- `GET /api/tasks` - List all tasks
- `GET /api/tasks/{id}` - Get task by ID
- `POST /api/tasks` - Create new task
- `PUT /api/tasks/{id}` - Update task
- `DELETE /api/tasks/{id}` - Delete task

### Health
- `GET /health` - Health check endpoint

## Development

### Running Tests
```bash
pytest
```

### Linting
```bash
ruff check .
black .
```

### Database Migrations
```bash
# Create new migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

## Dependencies

Core:
- FastAPI - Modern web framework
- Uvicorn - ASGI server
- SQLAlchemy - ORM
- Pydantic - Data validation
- Alembic - Database migrations

External Services:
- PostgreSQL - Primary database
- Redis - Caching and sessions
- SendGrid - Email delivery
- AWS S3 - File storage
- Stripe - Payment processing
- OpenAI - AI features

Utilities:
- schema-validate - Database schema validation

## License

MIT
```

---

## Final Folder Structure:
```
.
├── schema-validate/
│   ├── setup.py
│   ├── schema_validate/
│   │   └── __init__.py
│   ├── README.md
│   └── LICENSE
│
└── taskflow-test/
    ├── .env
    ├── .gitignore
    ├── requirements.txt
    ├── README.md
    ├── main.py
    ├── config.py
    ├── database.py
    └── models.py