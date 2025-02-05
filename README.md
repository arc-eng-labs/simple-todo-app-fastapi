# Todo App (Python 11, FastAPI, SQLite, Poetry)

## Overview

This is a simple Todo application developed using:

- **Python 11**
- **FastAPI** (for building the REST API)
- **SQLite** (as the database)
- **Poetry** (for dependency management)

It includes a minimal user interface served via static files, allowing you to view, create, and manage tasks.

## Key Features

- Basic CRUD functionality using FastAPI.
- SQLite database for storage (no migrations necessary).
- Simple UI using HTML, CSS, and JavaScript.

## Project Structure

```
.
├── README.md                # Project overview and documentation
├── pyproject.toml           # Poetry configuration (dependencies, project metadata)
├── app
│   ├── main.py              # Entry point: sets up FastAPI app and routes
│   ├── database.py          # Database connection using SQLAlchemy
│   ├── models.py            # Defines the SQLite models with SQLAlchemy
│   ├── schemas.py           # Pydantic schemas for request/response models
│   └── crud.py              # CRUD operations
└── static
    ├── index.html           # UI page
    ├── style.css            # Styles for the UI
    └── script.js            # Client-side logic for interacting with the API
```

## Getting Started

1. **Install Poetry** (if not already installed)
   - Refer to [Poetry's official docs](https://python-poetry.org/docs/#installation) for instructions.

2. **Install Project Dependencies**:
   ```bash
   poetry install
   ```

3. **Run the Application**:
   ```bash
   poetry run uvicorn app.main:app --reload
   ```
   The application will start on `http://127.0.0.1:8000`.

4. **Open the UI**:
   - Open `http://127.0.0.1:8000/index.html` in your browser.
   - Create, read, update, and delete tasks from the interface.

## Usage

- **List Tasks**: On the UI, all tasks in the database are displayed.
- **Create Task**: Use the text input to add a new task.
- **Update Task**: Check a task to mark it complete.
- **Delete Task**: Click the delete button to remove a task.


## License

This project is licensed under the MIT License.

---

Enjoy your new Todo application!
