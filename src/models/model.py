from pydantic import BaseModel

class Person(BaseModel):
    name: str
    email: str
    profession: str
    phonenumber: str
    linkedin: str
    github: str
    address: str
      