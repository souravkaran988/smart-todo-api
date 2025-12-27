from motor.motor_asyncio import AsyncIOMotorClient

# Replace the string below with your actual connection string from Atlas
# Make sure your username and password are correct inside the string!
MONGO_DETAILS = "mongodb+srv://karansourav453_db_user:yWWV210OHpk4dTLq@smarttodo.97nqxp0.mongodb.net/?appName=SmartToDo"

client = AsyncIOMotorClient(MONGO_DETAILS)

# This creates/connects to a database named 'todo_db'
database = client.todo_db

# This creates/connects to a collection (table) named 'tasks'
task_collection = database.get_collection("tasks")

# Helper function to format MongoDB results
def task_helper(task) -> dict:
    return {
        "id": str(task["_id"]),
        "title": task["title"],
        "description": task["description"],
        "completed": task["completed"],
    }

user_collection = database.get_collection("users")

def user_helper(user) -> dict:
    return {
        "id": str(user["_id"]),
        "fullname": user["fullname"],
        "email": user["email"],
    }