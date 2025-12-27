from pydantic import BaseModel, Field
from typing import Optional

# This defines how a Task looks when a user creates it
class TaskSchema(BaseModel):
    title: str = Field(...)
    description: Optional[str] = None
    completed: bool = False

    class Config:
        # Example data for the Swagger UI
        json_schema_extra = {
            "example": {
                "title": "Buy groceries",
                "description": "Milk, Eggs, and Bread",
                "completed": False
            }
        }