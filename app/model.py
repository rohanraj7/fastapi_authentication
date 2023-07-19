from pydantic import BaseModel, Field, EmailStr


class PostSchema(BaseModel):
    id : int = Field(default=None, example=1)
    title : str = Field(default=None, example="some title about animals")
    content : str = Field(default=None, example="some content about animals")
    class Config:
        schema_extra = {
            "post_demo": {
                "title": "some title about annimals",
                "content": "some content about animals"
            }
        }

class UserSchema(BaseModel):
    fullname : str = Field(default= None)
    email: EmailStr =  Field(default=None)
    password: str = Field(default=None)
    class Config:
        schema_extra = {
            "user_demo": {
                "name": "Bek",
                "email": "help@bekbrace.com",
                "password": "123"
            }
        }

class UserLoginSchema(BaseModel):
    email: EmailStr =  Field(default=None)
    password: str = Field(default=None)
    class Config:
        schema_extra = {
            "user_demo": {
                "email": "help@bekbrace.com",
                "password": "123"
            }
        }
