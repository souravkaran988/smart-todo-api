from fastapi import FastAPI, Body, Depends, HTTPException
from bson import ObjectId

# Import from our other project files
from database import task_collection, task_helper, user_collection
from models import TaskSchema
from auth_models import UserSchema, UserLoginSchema
from auth_handler import sign_jwt, get_password_hash, verify_password
from auth_bearer import JWTBearer

app = FastAPI()

# --- ROOT ROUTE ---
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Smart ToDo API!"}

# --- USER AUTHENTICATION ROUTES ---

@app.post("/user/signup", tags=["user"])
async def create_user(user: UserSchema = Body(...)):
    # 1. Check if email already exists
    existing_user = await user_collection.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # 2. Convert to dict and hash password
    user_data = user.model_dump()
    user_data["password"] = get_password_hash(user.password)
    
    # 3. Insert into database
    await user_collection.insert_one(user_data)
    
    # 4. Return token
    return sign_jwt(user.email)

@app.post("/user/login", tags=["user"])
async def user_login(user: UserLoginSchema = Body(...)):
    found_user = await user_collection.find_one({"email": user.email})
    
    if found_user:
        if verify_password(user.password, found_user["password"]):
            return sign_jwt(user.email)
    
    raise HTTPException(status_code=403, detail="Wrong login details")

# --- TASK CRUD ROUTES (PROTECTED) ---

# All routes below now require a valid JWT Token passed in the Header

@app.post("/tasks", tags=["tasks"], dependencies=[Depends(JWTBearer())])
async def add_task(task: TaskSchema = Body(...)):
    new_task = await task_collection.insert_one(task.model_dump())
    created_task = await task_collection.find_one({"_id": new_task.inserted_id})
    return task_helper(created_task)

@app.get("/tasks", tags=["tasks"], dependencies=[Depends(JWTBearer())])
async def get_tasks():
    tasks = []
    async for task in task_collection.find():
        tasks.append(task_helper(task))
    return tasks

@app.put("/tasks/{id}", tags=["tasks"], dependencies=[Depends(JWTBearer())])
async def update_task(id: str, data: TaskSchema = Body(...)):
    updated_task = await task_collection.update_one(
        {"_id": ObjectId(id)}, {"$set": data.model_dump()}
    )
    if updated_task.modified_count == 1:
        return {"message": "Task updated successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{id}", tags=["tasks"], dependencies=[Depends(JWTBearer())])
async def delete_task(id: str):
    delete_result = await task_collection.delete_one({"_id": ObjectId(id)})
    if delete_result.deleted_count == 1:
        return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")