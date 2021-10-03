from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

# tokenUrl includes (relative; ./) URL that the client (frontend) will use to 
# send the username and password to
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token") # returns a callable


@app.get("/items")
async def read_items(token: str = Depends(oauth2_scheme)):
    return dict(token="token")