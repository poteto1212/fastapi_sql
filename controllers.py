from re import template
from fastapi import FastAPI, Body
from starlette.templating import Jinja2Templates
from starlette.requests import Request

import sqlalchemy

engine = sqlalchemy.create_engine(
    'mysql+pymysql://root:Makt0112pc-49466@localhost:3306/db_fastapi')


app = FastAPI(
    title='FastAPIでつくるtoDoアプリケーション',
    description='FastAPIチュートリアル：FastAPI(とstarlette)でシンプルなtoDoアプリを作りましょう．',
    version='0.9 beta'
)


templates = Jinja2Templates(directory="templates")
jinja_env = templates.env


def index(request: Request):
    return templates.TemplateResponse('index.html',
                                      {'request': request, 'abc': 'タイトル', }
                                      )


@app.get('/home')
def home(request: Request):
    homelist = engine.execute(
        "SELECT * FROM Post"
    )
    return templates.TemplateResponse('home.html',
                                      {'request': request,
                                       'lists': homelist}
                                      )


@app.get('/new')
def home(request: Request):
    return templates.TemplateResponse('new.html',
                                      {'request': request}
                                      )


@app.post("/create")
def create(username: str = Body(...), content: str = Body(...)):
    engine.execute(
        f"INSERT INTO Post (username,content) VALUES ('{username}','{content}')")


@app.get("/delete_wearning")
def delete_wearning(request: Request):
    return templates.TemplateResponse('warning.html',
                                      {'request': request}
                                      )


@app.get("/delete")
def delete(request: Request):
    engine.execute(
        ' DELETE FROM Post'
    )
    return templates.TemplateResponse('home.html',
                                      {'request': request}
                                      )
