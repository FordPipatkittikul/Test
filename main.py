from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

# POST: to create data.
# GET: to read data.
# PUT: to update data.
# DELETE: to delete data.


app = FastAPI()

students = {
    1 : {
        "name" : "John",
        "age" : 17,
        "year": "year 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UppdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None



@app.get("/")
async def index() -> dict:
    return {"name": "First Data"}

# path parameters
# gt mean input should be greater than
@app.get("/get-by-student-id/{student_id}")
async def get_student(student_id: int = Path(description="The ID of the student you want to view",gt=0)):
    return students[student_id]

# query parameter
@app.get("/get-by-name")
async def get_student(name : Optional[str] = None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

# test : int is parameter with default value.
# Optional[str] = None is parameter without default value.
# parameter with default value cannot follow parameter without default value unless we type *
@app.get("/path-and-query/{student_id}")
async def path_and_query(*,student_id: int, name : Optional[str] = None, test : int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}


@app.post("/create-student/{student_id}")
async def create_student(student_id : int, student : Student):
    if student_id in students:
        return {"Error": "Student exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
async def update_student(student_id: int, student: UppdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age= student.age
    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete-student/{student_id}")
async def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student does not exist"}
    del students[student_id]
    return {"Message": "Student deleted successfully"}