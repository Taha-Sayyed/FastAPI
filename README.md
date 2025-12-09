# FastAPI Learning Journey 🚀

Learning FastAPI and building RESTful APIs through hands-on projects.

**Course:** [FastAPI - The Complete Course](https://www.udemy.com/course/fastapi-the-complete-course/) by Eric Roby

---

## Projects

### Project 1: REST API Fundamentals
Building a book management API with core REST operations:
- **GET** - Retrieve books (path & query parameters)
- **POST** - Create new books
- **PUT** - Update existing books
- **DELETE** - Remove books

*Learning focus: HTTP methods, parameter types, basic CRUD operations*

### Project 2: Data Validation & Models
Enhancing the API with structured data validation:
- Pydantic models for request validation
- Field constraints (min/max length, ranges)
- Custom Book class with auto-generated IDs
- Better code organization

*Learning focus: Data validation, Pydantic, model design*

---

## Getting Started

```bash
# Install dependencies
uv sync

# Run a project
uvicorn Project-1.books:app --reload
# or
uvicorn Project-2.books:app --reload
```

Visit `http://localhost:8000/docs` for interactive API documentation.

---

## Progress Tracker

- ✅ Basic REST endpoints
- ✅ Path vs Query parameters
- ✅ Request body handling
- ✅ Pydantic validation
- 🔄 Next: Database integration

---

*Keep building, keep learning! 💪*

