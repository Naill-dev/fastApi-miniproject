from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Sadə məlumat bazası əvəzi (In-memory)
data_store = [
    {"id": 1, "item": "Python öyrən", "status": "davam edir"},
    {"id": 2, "item": "FastAPI layihəsi", "status": "gözləmədə"}
]

# Validasiya üçün model
class Task(BaseModel):
    item: str
    status: Optional[str] = "aktiv"

@app.get("/")
def home():
    return {"status": "Online", "message": "FastAPI Mini Service"}

@app.get("/tasks")
def get_all_tasks():
    return data_store

@app.post("/tasks")
def add_task(task: Task):
    new_id = len(data_store) + 1
    new_task = {"id": new_id, **task.model_dump()}
    data_store.append(new_task)
    return new_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    global data_store
    data_store = [t for t in data_store if t["id"] != task_id]
    return {"message": f"ID {task_id} silindi"}
