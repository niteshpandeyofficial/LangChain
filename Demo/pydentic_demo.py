from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name:str
    age:int
    address: Optional[str]=None
    email:EmailStr   #email validator
    cgpa:float =Field(gt=0,lt=10,default=5,description="Deecimal value represent the student CGPA ")


# stud1={'name':"nitesh",'age':34,"email":'nitesh@gmail.com'} #default cgpa set as 5 in this case
stud1={'name':"nitesh",'age':34,"email":'nitesh@gmail.com','cgpa':'9'}
# stud1={'name':"nitesh",'age':34,"email":'nitesh@gmail.com','cgpa':9}
# stud1={'name':"nitesh",'age':34,'email':'abc@gmail.com'} #validate that the email is valid
# stud1={'name':456,'age':34} #this code will give the type error
student=Student(**stud1)
print(student)
print(student.address)
print(student.age)
print(student.name)