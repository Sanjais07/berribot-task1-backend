

# **Berribot Backend**

This is the FastAPI backend for the Berribot Employee Login System. It provides RESTful API endpoints for user registration, login, and listing registered employees. The backend interacts with a PostgreSQL database for persistent data storage and communicates with a React.js frontend.

---

## **Features**

* User registration with email and password
* Login validation with token generation
* Fetch all registered users
* Error handling for duplicate entries and invalid credentials
* Configured CORS to allow frontend-backend communication

---

## **Technologies Used**

* **FastAPI** – high-performance web framework for Python
* **PostgreSQL** – relational database for storing user data
* **psycopg2** – PostgreSQL database adapter for Python
* **Pydantic** – for data validation
* **Uvicorn** – ASGI server to run FastAPI apps

---

## **Folder Structure**

```
server/
├── main.py               # Entry point for FastAPI app
├── auth.py               # Handles DB connection and authentication logic
├── models.py             # Pydantic models for request schemas
```

---

## **Setup Instructions**

### 1. Clone the repository:

```bash
git clone <your-repo-url>
cd berribot-backend
```

### 2. Create a virtual environment and activate it:

```bash
python -m venv env
source env/bin/activate     # Linux/macOS
env\Scripts\activate        # Windows
```

### 3. Install dependencies:

```bash
pip install fastapi uvicorn psycopg2 pydantic
```

### 4. Set up PostgreSQL Database:

* Create a database named `NewDB`
* Make sure PostgreSQL is running on `localhost:5432`
* Update connection credentials if needed in `auth.py`

### 5. Run the backend server:

```bash
uvicorn main:app --reload
```

The backend will be available at:

```
http://localhost:8000
```

---

## **API Endpoints**

* `POST /register` – Register a new user
* `POST /login` – Authenticate user and return token
* `GET /users` – Retrieve list of all registered user emails

---

## Screenshots:

![image](https://github.com/user-attachments/assets/28a5c471-a721-49df-9dd9-26b8ea913d47)
![image](https://github.com/user-attachments/assets/85d637eb-4d92-403a-8419-9e0ef3268c8b)

