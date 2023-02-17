from fastapi import Query, APIRouter
from fastapi.responses import JSONResponse
from config.database import Session
from models.users import User as UserModel
from typing import  List
from fastapi.encoders import jsonable_encoder
from services.users import UserService
from schemas.forms import User

forms_router = APIRouter()

@forms_router.post('/login', tags=['Login'], response_model=dict, status_code=201)
def create_user(user: User) -> dict:
    db = Session()
    UserService(db).create_user(user)
    return JSONResponse(status_code=201, content={'message': 'Registro exitoso'})

@forms_router.get('/users', tags=['Users'], response_model=List[User], status_code=200)
def get_users() -> List [User]:
    db = Session()
    result = UserService(db).get_users()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@forms_router.get('/users/{Name}', tags=['Users'], response_model=User)
def get_users_name(name: str) -> User:
    db = Session()
    result = UserService(db).get_user(name)
    if not result:
        return JSONResponse(status_code=404, content={'message': 'User no encontrado'})
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
