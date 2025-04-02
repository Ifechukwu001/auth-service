from pydantic import BaseModel, EmailStr

from src.api.typing.PasswordValidator import IsStrongPassword


class PasswordResetRequest(BaseModel):
    email: EmailStr

class ConfirmPasswordResetRequest(BaseModel):
    reset_token: str
    new_password: IsStrongPassword