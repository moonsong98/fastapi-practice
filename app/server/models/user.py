from typing import Optional
from pydantic import BaseModel, EmailStr, Field

class UserSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    height: int = Field(...)
    weight: int =  Field(...)

    class Config:
        shema_extra = {
                "example" : {
                        "fullname": "Moon Kyung Song",
                        "email": "moonsong98@postech.ac.kr",
                        "height": 177,
                        "weight": 70,
                    }
                }

class UpdateUserModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    height: Optional[int]
    weight: Optional[int]

    class Config:
        schema_extra = {
                "example": {
                        "fullname": "Moon Kyung Song",
                        "email": "moonsong98@postech.ac.kr",
                        "height": 177,
                        "weight": 70,
                    }
                }


def ResponseModel(data, message):
    return {
            "data": [data],
            "code": 200,
            "message": message,
            }

def ErrorResponseModel(error, code, message):
    return {"error": error, "code": code, "message": message}
