"""
TaskFlow API - Main application entry point
"""
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI(
    title="TaskFlow API",
    description="Task management system with real-time updates",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# In-memory storage (for demo purposes)
tasks_db = []
task_id_counter = 1

# Pydantic models
class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: Optional[str] = None
    completed: bool = False
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None

# Routes
@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to TaskFlow API",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy"}

@app.get("/api/tasks", response_model=List[Task])
async def get_tasks():
    """Get all tasks"""
    return tasks_db

@app.get("/api/tasks/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Get a specific task"""
    task = next((t for t in tasks_db if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.post("/api/tasks", response_model=Task, status_code=201)
async def create_task(task: TaskCreate):
    """Create a new task"""
    global task_id_counter
    
    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "description": task.description,
        "completed": False,
        "created_at": datetime.now(),
        "updated_at": datetime.now()
    }
    
    tasks_db.append(new_task)
    task_id_counter += 1
    
    return new_task

@app.put("/api/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: TaskUpdate):
    """Update a task"""
    task = next((t for t in tasks_db if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    if task_update.title is not None:
        task["title"] = task_update.title
    if task_update.description is not None:
        task["description"] = task_update.description
    if task_update.completed is not None:
        task["completed"] = task_update.completed
    
    task["updated_at"] = datetime.now()
    
    return task

@app.delete("/api/tasks/{task_id}")
async def delete_task(task_id: int):
    """Delete a task"""
    global tasks_db
    task = next((t for t in tasks_db if t["id"] == task_id), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks_db = [t for t in tasks_db if t["id"] != task_id]
    
    return {"message": "Task deleted successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)