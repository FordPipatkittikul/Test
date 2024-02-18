from pydantic import BaseModel

class Student(BaseModel):
    name: str
    age: 12

print(Student.age)
