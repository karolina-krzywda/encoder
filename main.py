import secrets

from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import uvicorn
from starlette import status

from app.utils.CesarCipher import CesarCipher

app = FastAPI()

cipher = CesarCipher(4)

security = HTTPBasic()
auth = ('user', 'secret123')


@app.get("/encode/{text}")
def encode(text: str, credentials: HTTPBasicCredentials = Depends(security)):
    """Encode passed string"""
    raise_unauthorized_when_bad_credentials(credentials)
    return {"result": f"{cipher.encode(text)}"}


@app.get("/decode/{text}")
def decode(text: str, credentials: HTTPBasicCredentials = Depends(security)):
    """Decode passed string"""
    raise_unauthorized_when_bad_credentials(credentials)
    return {"result": f"{cipher.decode(text)}"}


def raise_unauthorized_when_bad_credentials(credentials):
    if not is_user_authorized(credentials):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect user or password"
        )


def is_user_authorized(credentials: HTTPBasicCredentials):
    return secrets.compare_digest(auth[0], credentials.username) and \
           secrets.compare_digest(auth[1], credentials.password)


if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info")
