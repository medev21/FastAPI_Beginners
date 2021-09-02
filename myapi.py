from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI() # create instance of fastapi object

students = {
    1: {
        "name": "John",
        "age": 17,
        "year": "Year 12"
    }
}

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return {"name": "First Data"};

# path route
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(None, description="The ID of the student you want  to view", gt=0)): # gt greater than 0
    return students[student_id]

# query route
# @app.get("/get-by-name")
# def get_student(*, name: Optional[str] = None, test: int):

#     for student_id in students:
#         if students[student_id]["name"] == name:
#             return students[student_id];

#     return {"Data": "Not found"}

# path and query combined
@app.get("/get-by-name/{student_id}")
def get_student(*,student_id: int, name: Optional[str] = None, test: int):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id];

    return {"Data": "Not found"}

# request body and post method
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}

    students[student_id] = student
    return students[student_id]

# put method
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student does not exist!"}

    if student.name != None:
        students[student_id].name = student.name

    if student.age != None:
        students[student_id].age = student.age

    if student.year != None:
        students[student_id].year = student.year

    return students[student_id]

@app.delete("/delete/{student_id}")
def delete_user(student_id):
    if student_id not in students:
        return {"Error": "Student does not exist!"}

    del students[student_id]
    return {"Message": "User has been deleted successfully"}

# to run app -> `uvicorn myapi:app --reload`