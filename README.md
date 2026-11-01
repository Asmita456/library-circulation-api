# Library Circulation API

A RESTful API for managing library records, developed using Python, FastAPI, SQLModel, SQLAlchemy, SQLite, and PostgreSQL.

This project demonstrates how to build a backend application using FastAPI, connect to relational databases, and perform book management, borrowing, returning, and reporting operations using SQLModel and SQLAlchemy.

## 1. Project Description

The Library Circulation API is a backend application developed using Python and FastAPI. It provides REST API endpoints to create, retrieve, update, and delete book records, manage book loans, and generate library summary reports.

The application uses SQLModel and SQLAlchemy for database interaction and SQLite as the default database. It also supports PostgreSQL through environment-based database configuration.

The application provides automatic database table creation, database session management, request validation, transaction handling, and error handling.

## 2. Technologies Used

**Python:** Programming language used to develop the application.

**FastAPI:** Modern Python framework used to build REST APIs.

**SQLModel:** ORM library used for database models, validation, and database operations.

**SQLAlchemy:** SQL toolkit and ORM that powers database operations through SQLModel.

**SQLite:** Lightweight relational database used as the default database.

**PostgreSQL:** Relational database supported as an alternative database.

**Psycopg:** PostgreSQL adapter used to connect Python applications to PostgreSQL.

**Python-dotenv:** Library used to load database configuration from environment variables.

**Uvicorn:** ASGI server used to run the FastAPI application.

## 3. Project Structure

'''
library_circulation_api/
│
├── app/
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── books.py
│   │   ├── loans.py
│   │   └── reports.py
│   │
│   ├── __init__.py
│   ├── database.py
│   ├── main.py
│   ├── models.py
│   └── schemas.py
│
├── screenshots/
│   ├── book_not_found.png
│   ├── create_book.png
│   ├── delete_book.png
│   ├── get_book_by_id.png
│   ├── get_books.png
│   ├── library_api_swagger.png
│   ├── loan_book_not_found.png
│   └── loan_create.png
│
├── venv/
│
├── .env
├── .gitignore
├── library.db
├── README.md
└── requirements.txt
'''
### File Description

**__init__.py:** Marks the app and routers directories as Python packages, allowing their modules to be imported.

**database.py:** Handles database connections, engine creation, automatic table creation, and database session management.

**main.py:** Creates the FastAPI application, initializes the database using the application lifespan, and includes the book, loan, and report routers.

**models.py:** Defines the Book and Loan database tables and their relationships.

**schemas.py:** Defines request validation schemas for creating and updating books and creating loans.

**books.py:** Contains all book management API endpoints, including creating, retrieving, updating, deleting, searching, and filtering books.

**loans.py:** Contains loan management endpoints for borrowing and returning books, including available-copy updates.

**reports.py:** Contains the library summary report endpoint.

**requirements.txt:** Contains the required Python packages.

**README.md:** Provides project documentation, installation instructions, and API details.

**.gitignore:** Specifies files and folders that should not be tracked by Git.

**.env:** Stores database configuration using environment variables. It should not be uploaded to GitHub.

**library.db:** SQLite database file used to store book and loan records during local SQLite development.

## 4. Features

- Create a new book record.
- Retrieve all book records.
- Retrieve an individual book using its ID.
- Update existing book information.
- Delete a book if it has no loan history.
- Borrow books using their book ID.
- Return borrowed books.
- Automatically decrease available copies when a book is borrowed.
- Automatically increase available copies when a book is returned.
- Prevent borrowing when no copies are available.
- Prevent returning the same loan more than once.
- Retrieve all loan records.
- Retrieve only active loans.
- Search books by title or author.
- Filter books by category.
- Filter books by availability.
- Combine multiple book filters.
- Generate library summary reports.
- SQLite and PostgreSQL database connectivity.
- Automatic database table creation.
- Database session management.
- Request data validation.
- Transaction handling for borrowing and returning books.
- Error handling for missing records and conflicting operations.
- Interactive API documentation using Swagger UI.

## 5. Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/Asmita456/library-circulation-api.git
```

### Step 2: Navigate to the Project Folder

```bash
cd library-circulation-api
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate
```

For Linux/macOS:

```bash
source venv/bin/activate
```

### Step 5: Install Required Packages

```bash
pip install -r requirements.txt
```

The required packages include:

```text
fastapi
uvicorn
sqlmodel
sqlalchemy
psycopg[binary]
python-dotenv
```

SQLAlchemy is also installed as a dependency of SQLModel.

### Step 6: Configure the Database

Create a `.env` file in the main project directory.

For SQLite:

```env
DATABASE_URL=sqlite:///./library.db
```

For PostgreSQL:

```env
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/library_db
```

Replace `YOUR_PASSWORD` with your PostgreSQL password.

The application uses SQLite by default when no DATABASE_URL environment variable is provided.

**Note:** The `.env` file contains database credentials and should not be committed to Git.

## 6. Run the Application

Run the following command from the main project directory:

```bash
fastapi dev
```

Alternatively, use:

```bash
uvicorn app.main:app --reload
```

The application will run at:

**Base URL:**

```text
http://127.0.0.1:8000
```

**Swagger UI:**

```text
http://127.0.0.1:8000/docs
```

**ReDoc:**

```text
http://127.0.0.1:8000/redoc
```

To stop the server, press `Ctrl + C`.

## 7. API Documentation

FastAPI automatically generates interactive API documentation using Swagger UI.

Open the following URL in your browser:

```text
http://127.0.0.1:8000/docs
```

Through Swagger UI, users can:

- View all available API endpoints.
- Understand the required request parameters.
- Submit JSON request bodies.
- Execute book management operations.
- Execute borrowing and returning operations.
- Search and filter books.
- Generate library summary reports.
- View API responses and HTTP status codes.

## 8. API Endpoints

The application provides the following API endpoints:

### Book Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/books/` | Create a new book |
| GET | `/books/` | Retrieve all books |
| GET | `/books/{book_id}` | Retrieve a book by ID |
| PATCH | `/books/{book_id}` | Update book information |
| DELETE | `/books/{book_id}` | Delete a book by ID |

### Loan Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/loans/` | Borrow a book |
| GET | `/loans/` | Retrieve all loans |
| PATCH | `/loans/{loan_id}/return` | Return a borrowed book |

### Report Endpoint

| Method | Endpoint | Description |
|---|---|---|
| GET | `/reports/summary` | Retrieve library summary |

### Book Filtering

The GET `/books/` endpoint supports the following query parameters:

| Parameter | Description |
|---|---|
| `search` | Search books by title or author |
| `category` | Filter books by category |
| `available_only` | Display only books with available copies |

Example:

```text
/books/?search=Python&category=Programming&available_only=true
```

### Active Loan Filtering

The GET `/loans/` endpoint supports the `active_only` parameter.

Example:

```text
/loans/?active_only=true
```

This endpoint retrieves only loans that have not yet been returned.

## 9. Sample API Requests

### 1. Create a Book

**Method:** POST

**Endpoint:** `/books/`

**Request Body:**

```json
{
  "title": "Python Basics",
  "author": "John Smith",
  "category": "Programming",
  "total_copies": 3
}
```

This endpoint creates a new book record in the database.

The book ID is generated automatically, and the `available_copies` value is initialized to the same value as `total_copies`.

**Example Response:**

```json
{
  "total_copies": 3,
  "title": "Python Basics",
  "author": "John Smith",
  "category": "Programming",
  "id": 1,
  "available_copies": 3
}
```

### 2. Get All Books

**Method:** GET

**Endpoint:** `/books/`

No request body is required.

This endpoint retrieves all book records stored in the database.

### 3. Get Book by ID

**Method:** GET

**Endpoint:** `/books/1`

No request body is required.

This endpoint retrieves the book whose ID is 1.

### 4. Update Book Information

**Method:** PATCH

**Endpoint:** `/books/1`

**Request Body:**

```json
{
  "title": "Python Advanced"
}
```

This endpoint updates only the specified book information.

The other fields remain unchanged.

### 5. Delete a Book

**Method:** DELETE

**Endpoint:** `/books/1`

No request body is required.

This endpoint deletes a book if it has no loan history.

If the book has previous loan records, the API returns a `409 Conflict` response.

### 6. Borrow a Book

**Method:** POST

**Endpoint:** `/loans/`

**Request Body:**

```json
{
  "book_id": 1,
  "borrower_name": "Aarati"
}
```

This endpoint creates a new loan record for the selected book.

When a book is borrowed, its available copies decrease by one.

**Example Response:**

```json
{
  "borrower_name": "Aarati",
  "book_id": 1,
  "id": 1,
  "is_returned": false
}
```

### 7. Get All Loans

**Method:** GET

**Endpoint:** `/loans/`

This endpoint retrieves all loan records stored in the database.

### 8. Return a Book

**Method:** PATCH

**Endpoint:** `/loans/1/return`

No request body is required.

This endpoint marks the selected loan as returned and increases the available copies of the corresponding book by one.

**Example Response:**

```json
{
  "borrower_name": "Aarati",
  "book_id": 1,
  "id": 1,
  "is_returned": true
}
```

### 9. Get Library Summary

**Method:** GET

**Endpoint:** `/reports/summary`

No request body is required.

This endpoint provides an overview of the library.

**Example Response:**

```json
{
  "total_books": 1,
  "total_copies": 3,
  "available_copies": 3,
  "active_loans": 0
}
```

## 10. Database Structure

This project uses SQLModel and SQLAlchemy for database operations.

SQLite is the default database, and PostgreSQL is also supported.

The application automatically creates the required database tables when it starts.

### Book Table

| Field | Data Type | Description |
|---|---|---|
| id | Integer | Primary key and unique book identifier |
| title | String | Title of the book |
| author | String | Author of the book |
| category | String | Category of the book |
| total_copies | Integer | Total number of book copies |
| available_copies | Integer | Number of currently available copies |

### Loan Table

| Field | Data Type | Description |
|---|---|---|
| id | Integer | Primary key and unique loan identifier |
| book_id | Integer | Foreign key referencing the Book table |
| borrower_name | String | Name of the person borrowing the book |
| is_returned | Boolean | Indicates whether the book has been returned |

### Database Operations

**Database Engine:** Creates a connection between the application and the selected database.

**Database Session:** Manages communication between API endpoints and the database.

**SQLModel:** Defines database models and performs database operations.

**SQLAlchemy:** Provides the underlying ORM and SQL database functionality.

**SQLite:** Stores book and loan records in the `library.db` file.

**PostgreSQL:** Provides an alternative relational database connection through the DATABASE_URL configuration.

## 11. Error Handling

The API handles different error situations and returns appropriate HTTP status codes.

| Status Code | Description |
|---|---|
| 200 | Request successful |
| 201 | Resource created successfully |
| 204 | Resource deleted successfully |
| 404 | Requested book or loan not found |
| 409 | Conflict, such as unavailable copies, duplicate return, or loan history |
| 422 | Request validation error |

### Example 404 Response

When a user requests a book that does not exist:

```json
{
  "detail": "Book not found"
}
```

### Example 409 Response

When a user tries to return the same loan more than once:

```json
{
  "detail": "Book already returned"
}
```

When a user tries to delete a book with loan history:

```json
{
  "detail": "Book has loan history"
}
```

FastAPI also provides automatic request validation and returns appropriate validation errors when invalid data is submitted.

## 12. Application Workflow

The application follows a structured workflow:

1. The user sends an HTTP request to a FastAPI endpoint.
2. FastAPI receives the request and validates the submitted data.
3. The appropriate router processes the requested operation.
4. A database session is provided through FastAPI dependency injection.
5. SQLModel and SQLAlchemy perform the required database operations.
6. The selected database stores or retrieves the records.
7. The API returns the appropriate response and HTTP status code.

### Role of Each Application File

**main.py:** Initializes the FastAPI application, database, and API routers.

**database.py:** Manages database connections, engine creation, and database sessions.

**models.py:** Defines the Book and Loan database models.

**schemas.py:** Defines request validation schemas.

**books.py:** Handles book creation, retrieval, updating, deletion, searching, and filtering.

**loans.py:** Handles book borrowing, loan retrieval, and book returns.

**reports.py:** Generates library summary information.

**__init__.py:** Identifies the application and routers directories as Python packages.

## 13. Testing

The API was tested using the interactive Swagger UI.

The following operations were tested:

- Creating a book successfully.
- Borrowing a book successfully.
- Checking available copies after borrowing.
- Returning a borrowed book.
- Restoring available copies after returning.
- Preventing duplicate book returns.
- Searching books by title.
- Filtering books by category.
- Filtering books by availability.
- Updating book information.
- Preventing deletion of books with loan history.
- Validating incorrect book information.
- Handling requests for missing book IDs.
- Generating the library summary report.
- Connecting to PostgreSQL and creating database tables.

The tested API responses included `200`, `201`, `409`, and `422` status codes. The missing-book request also returned the expected `404` response body.

## 14. Conclusion

This project helped me understand how to develop RESTful APIs using FastAPI, connect relational databases using SQLModel and SQLAlchemy, manage database sessions, and perform database operations.

It also provided practical knowledge of API routing, request handling, data validation, database connectivity, transaction handling, error handling, and organizing a Python backend application into separate modules.

Overall, the Library Circulation API demonstrates the implementation of a backend application for managing books, borrowing and returning operations, and library reports using modern Python technologies.

## 15. Author

**Developed by:** Asmita Pandeya

**Project:** Library Circulation API


Developed as a practical assignment to understand REST API development, database integration, and backend application development using Python.