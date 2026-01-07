# FastAPI + SQLAlchemy CRUD Application

A RESTful API built with FastAPI and SQLAlchemy that demonstrates full CRUD (Create, Read, Update, Delete) operations for user management.

## Features

- ✅ Full CRUD operations for users
- ✅ SQLite database with SQLAlchemy ORM
- ✅ Pydantic models for request/response validation
- ✅ Automatic API documentation (Swagger UI)
- ✅ Type-safe endpoints with response models
- ✅ Database session management with dependency injection

## Project Structure

```
fast-api-sqlalchemy/
├── myapi.py              # Main FastAPI application with endpoints
├── database.py           # Database configuration and session management
├── database_models.py    # SQLAlchemy ORM models
├── models.py             # Pydantic models for validation
├── users.db              # SQLite database file
└── README.md             # This file
```

## Installation

1. **Install dependencies:**

   ```bash
   pip install fastapi sqlalchemy uvicorn pydantic
   ```

2. **Run the application:**

   ```bash
   uvicorn myapi:app --reload
   ```

3. **Access the API:**
   - API: http://localhost:8000
   - Interactive API docs (Swagger): http://localhost:8000/docs
   - Alternative API docs (ReDoc): http://localhost:8000/redoc

## API Endpoints

### Root

- **GET** `/` - Welcome message

### Users

#### Get All Users

- **GET** `/users/` - Retrieve all users
- **Response:** List of user objects

#### Get User by ID

- **GET** `/users/{user_id}` - Retrieve a specific user by ID
- **Response:** User object
- **Errors:** 404 if user not found

#### Create User

- **POST** `/users/` - Create a new user
- **Request Body:**
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "role": "admin"
  }
  ```
- **Response:** Created user object with generated ID
- **Errors:** 404 if user with email already exists

#### Update User

- **PUT** `/users/{user_id}` - Update an existing user
- **Request Body:** Same as Create User
- **Response:** Updated user object
- **Errors:** 404 if user not found

#### Delete User

- **DELETE** `/users/{user_id}` - Delete a user
- **Response:** Success message
- **Errors:** 404 if user not found

## Database Schema

### User Model

- `id` (Integer, Primary Key) - Auto-generated unique identifier
- `name` (String, 100 chars, Required) - User's name
- `email` (String, 100 chars, Required, Unique) - User's email address
- `role` (String, 100 chars, Required) - User's role

## Example Usage

### Create a User

```bash
curl -X POST "http://localhost:8000/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Doe",
    "email": "jane@example.com",
    "role": "user"
  }'
```

### Get All Users

```bash
curl "http://localhost:8000/users/"
```

### Get User by ID

```bash
curl "http://localhost:8000/users/1"
```

### Update User

```bash
curl -X PUT "http://localhost:8000/users/1" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Jane Smith",
    "email": "jane.smith@example.com",
    "role": "admin"
  }'
```

### Delete User

```bash
curl -X DELETE "http://localhost:8000/users/1"
```

## Technologies Used

- **FastAPI** - Modern, fast web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM for Python
- **Pydantic** - Data validation using Python type annotations
- **SQLite** - Lightweight database engine
- **Uvicorn** - ASGI server for running FastAPI applications

## Code Architecture

- **Separation of Concerns:** The code is organized into separate modules:

  - `database.py` handles database connection and session management
  - `database_models.py` defines SQLAlchemy ORM models
  - `models.py` defines Pydantic models for API validation
  - `myapi.py` contains the FastAPI application and route handlers

- **Dependency Injection:** Database sessions are managed using FastAPI's dependency injection system via `get_db()`

- **Type Safety:** All endpoints use Pydantic models for request/response validation, ensuring type safety and automatic API documentation
