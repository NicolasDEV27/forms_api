from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'FORMS API'
app.version = '0.0.1'

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('Todays date')

@app.post("/login/")
def login(username: str = Form(), password: str = Form()):
    return {"username": username}