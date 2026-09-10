from pydantic import BaseModel, EmailStr, Field

# Validates user registration inputs types, including email and password. 
# This ensures that the inputs meet the required format and constraints 
# before being processed or stored in the database.

class UserRegister(BaseModel):
    email: EmailStr
    password: str = Field(
        min_length=8,
        max_length=128,
    )

# Validates response output types, email only.

class UserResponse(BaseModel):
    id: int
    email: EmailStr

# Validates user login input types, including email and password.

class UserLogin(BaseModel):
email: EmailStr
password: str