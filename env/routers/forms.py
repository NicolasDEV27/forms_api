from fastapi import Query, APIRouter
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import Session
from models.users import User as UserModel
from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi.encoders import jsonable_encoder




forms_router = APIRouter()

class User(BaseModel):
    DNI: Optional[int] = None
    Name: str = Field(min_length=1, max_Length=20)
    Last_names: str = Field(min_length=1, max_Length=20)
    Age: int = Field(ge=1, le=100)
    Height: float = Field(ge=0.1, le=3)
    Birthday:  str = Field(min_Length=10, max_length=10)
    email: str = Field(min_length=1, max_Length=20)
    password: str = Field(min_length=1, max_Length=20)


@forms_router.get('/', tags=['Home'])
def message():
    return HTMLResponse('Todays date')

@forms_router.post('/login', tags=['Login'], response_model=dict, status_code=201)
def create_user(user: User) -> dict:
    db = Session()
    new_user = UserModel(**user.dict())
    db.add(new_user)
    db.commit()
    return JSONResponse(status_code=201, content={'message': 'Registro exitoso'})

@forms_router.get('/users', tags=['Users'], response_model=List[User], status_code=200)
def get_users() -> List [User]:
    db = Session()
    result = db.query(UserModel).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@forms_router.get('/users/', tags=['Users'], response_model=List[User], status_code=200)
def get_users_name( Name: str = Query(min_length=1, max_Length=20)) -> List [User]:
    db = Session()
    result = db.query(UserModel).filter(UserModel.Name == Name).all()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@forms_router.put('/users/{DNI})', tags=['Users'], response_model=dict, status_code=200)
def update_user(dni: int, user: User) -> dict:
    db = Session()
    result = db.query(UserModel).filter(UserModel.DNI == dni).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'User no encontrado'})
    result.Name = user.Name
    result.Last_names = user.Last_names
    result.Age = user.Age
    result.Height = user.Height
    result.Birthday = user.Birthday
    result.email = user.email
    result.password = user.password
    db.commit()
    return JSONResponse(status_code=200, content={'message': 'User modificado'})

@forms_router.delete('/users/{DNI})', tags=['Users'], response_model=dict, status_code=200)
def delete_user(dni: int) -> dict:
    db = Session()
    result = db.query(UserModel).filter(UserModel.DNI == dni).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': 'User no encontrado'})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={'message': 'User eliminado exitosamente'})
