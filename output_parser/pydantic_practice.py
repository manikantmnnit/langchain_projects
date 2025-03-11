from pydantic import BaseModel, EmailStr,PositiveInt,StrictBool,Field
from typing import Optional,List

class Person(BaseModel):
    name:list[str]
    age:PositiveInt=Field(gt=5,lt=30)
    email:Optional[EmailStr]=None
    job: StrictBool

data={
    'name':['mkk','rkk'],
    'age':'32',
    'job':False
}
person=Person(**data)
print(person)