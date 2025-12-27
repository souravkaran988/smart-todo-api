# 📝 Smart ToDo API – Backend Development Project

### 📌 Project Overview
This project implements a **robust RESTful Backend System** for task management. It allows users to securely manage their ToDo lists with full CRUD capabilities, backed by a cloud database.

The system features a complete **Authentication and Authorization** flow, ensuring that user data is private and tasks are only accessible to their respective owners.

### 🎯 Problem Statement
* **Input**: User credentials for authentication; Task details (title, description) for management.
* **Output**: Secure JWT access tokens; Persistent task data stored in a NoSQL database.
* **Goal**: To build a secure, scalable API that demonstrates proficiency in modern backend frameworks, database integration, and security protocols.

### 🛠️ Technologies Used
* **Python 3.12+**
* **FastAPI** (Web Framework)
* **MongoDB Atlas** (NoSQL Database)
* **Motor** (Asynchronous MongoDB Driver)
* **JWT (JSON Web Tokens)** (Authentication)
* **Passlib (Bcrypt)** (Password Hashing)
* **Pydantic** (Data Validation)

### 📂 Project Structure
| File Name | Purpose |
| :--- | :--- |
| `main.py` | The entry point containing all API routes and logic. |
| `database.py` | MongoDB Atlas connection and helper functions. |
| `auth_handler.py` | JWT generation, decoding, and password hashing. |
| `auth_bearer.py` | Middleware "gate" to verify JWT tokens for protected routes. |
| `models.py` | Pydantic models for Task data validation. |
| `auth_models.py` | Pydantic models for User registration and login. |
| `requirements.txt` | List of dependencies required to run the project. |

### ⚙️ Installation & Execution

Follow these steps to run the project locally on your machine:

**1️⃣ Clone the Repository**
```bash
git clone [https://github.com/souravkaran988/smart-todo-api.git](https://github.com/souravkaran988/smart-todo-api.git)
cd smart-todo-api

**2️⃣ Create & Activate Virtual Environment**
Bash

python -m venv venv
# On Windows:
venv\Scripts\activate    
# On macOS/Linux:
source venv/bin/activate  
3️⃣ Install Required Dependencies

Bash

pip install -r requirements.txt
4️⃣ Run the Application Start the development server using Uvicorn:

Bash

uvicorn main:app --reload
The server will start at: http://127.0.0.1:8000

5️⃣ Access Interactive Documentation (Swagger UI) Once the server is running, the reviewer can access the interactive Swagger UI for testing all endpoints at: 👉 http://127.0.0.1:8000/docs

🧠 Model & Logic Explanation
1️⃣ JWT Authentication Flow

Secure Hashing: User passwords are never stored in plain text; they are hashed using Bcrypt for security.

Token Generation: Upon successful login, the system generates a JWT token with an expiration timestamp.

Security Middleware: The JWTBearer class intercepts requests to ensure a valid "Bearer" token is present before accessing tasks.

2️⃣ Database Logic

Async Connection: Uses Motor for non-blocking, asynchronous communication with MongoDB Atlas.

Data Integrity: Uses Pydantic schemas to validate data before it is written to the database.

📊 Project Requirements Fulfilled
[x] User Authentication: Implemented via JWT.

[x] Database Integration: Connected to MongoDB Atlas.

[x] CRUD Endpoints: POST, GET, PUT, and DELETE /tasks.

[x] README: Full Installation & Execution instructions included as per guidelines.

[x] Clean Repository: Organized structure for easy review.

👨‍💻 Author
Sourav Karan 🔗 GitHub: https://github.com/souravkaran988

If you found this project useful, feel free to star the repository!


---

### 🚀 To Finish this in VS Code:
1.  **Paste** that text into your `README.md`.
2.  **Save** the file.
3.  In your VS Code terminal, run:
    ```bash
    git add README.md
    git commit -m "Complete professional README"
    git push origin main
    ```

**Would you like me to show you how to check if your GitHub page looks correct after you push?**