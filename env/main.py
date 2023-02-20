from fastapi import Query, FastAPI
from config.database import engine, Base 
from middlewares.error_handler import error_handler
from routers.forms import forms_router

app = FastAPI()
app.title = 'FORMS API'
app.version = '0.0.1'

app.add_middleware(error_handler)
app.include_router(forms_router)

Base.metadata.create_all(bind=engine)








