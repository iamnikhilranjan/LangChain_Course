# Make a dictionary to store name of a student - make sure the name is string only. 

from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Student(BaseModel):

    name: str = 'nikhil' # default value is passed
    age: Optional[int] = None
    email: EmailStr
    cgpa: float = Field(gt=0, lt=10, description='A decimal value representing the cgpa of the student')

new_student = {'name':'nikhil', 'age': 22, 'email': 'abc@gmail.com'}
# new_student = {'name': 32} #throw error : Input should be a valid string.

student = Student(**new_student)


student_dict = dict(student)


print(student_dict['age'])

# print(type(student)) #Print type 