from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = 'FORMS API'
app.version = '0.0.1'

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse('Hello World')