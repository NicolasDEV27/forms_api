from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import Session, engine, Base 
from models.users import User as UserModel
from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi.encoders import jsonable_encoder



app = FastAPI()
app.title = 'FORMS API'
app.version = '0.0.1'

Base.metadata.create_all(bind=engine)

class User(BaseModel):
    DNI: Optional[int] = None
    Name: str = Field(min_length=1, max_Length=20)
    Last_names: str = Field(min_length=1, max_Length=20)
    Age: int = Field(ge=1, le=100)
    Height: float = Field(ge=0.1, le=3)
    Birthday:  str = Field(min_Length=10, max_length=10)
    email: str = Field(min_length=1, max_Length=20)
    password: str = Field(min_length=1, max_Length=20)


@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('Todays date')

@app.post('/login', tags=['Login'], response_model=dict, status_code=201)
def create_user(user: User) -> dict:
    db = Session()
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=201, content={'message': 'Registro exitoso'})

@app.get('/login', tags=['Users'], response_model=List[User], status_code=200)
def get_users() -> List [User]:
    db = Session()
    result = db.query(UserModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))



