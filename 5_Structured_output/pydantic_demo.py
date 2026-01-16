from pydantic import BaseModel, EmailStr, Field
from typing import Optional
class Student(BaseModel):
    name: str
    age: Optional[int] = None
    gpa: float
    email:  EmailStr
    cgpa: float = Field( gt=0.0, lt=10.0, default=5, description="Cumulative Grade Point Average between 0.0 and 10.0")

new_student = {'name':"Prashant",  'gpa':3.8, 'email':'prashant@example.com'}
student = Student(**new_student)
student_dict = dict(student)
print(student_dict['age'])

print(student.model_dump_json())