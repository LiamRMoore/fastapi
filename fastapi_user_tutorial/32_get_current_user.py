from typing import Optional

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

# tokenUrl includes (relative; ./) URL that the client (frontend) will use to 
# send the username and password to
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # returns a callable


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


def fake_decode_token(token):
    return User(
        username=token+"_fakedecoded", email="a@b.com", full_name="John Spartan"
    )


async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user