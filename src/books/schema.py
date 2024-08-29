from pydantic import BaseModel

class Book(BaseModel):
    id : int
    title : str
    author :str
    page :int 
    language:str
    published_year :str
