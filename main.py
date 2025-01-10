"""
cd my_fastapi_project\lab9
python -m uvicorn main:app --reload

http://127.0.0.1:8000/docs

 """

"""Основная программа"""
from fastapi import FastAPI, HTTPException, Depends, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session, sessionmaker
from models import User, Post
from engine import getengine

app = FastAPI()
pages = Jinja2Templates(directory="pages")

engine = getengine()
SessionLocal = sessionmaker(bind=engine)

def get_db():
    """Зависимость для получения сессии базы данных."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/users/create", response_class=HTMLResponse)
async def create_user_form(request: Request):
    """Возвращает форму для создания нового пользователя."""
    return pages.TemplateResponse("create_user.html", {"request": request})

@app.post("/users/create")
async def create_user(username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    """Создает нового пользователя."""
    db_user = User(username=username, email=email, password=password)
    db.add(db_user)
    db.commit()
    return {"message": "Пользователь добавлен"}

@app.get("/users/", response_class=HTMLResponse)
async def read_users(request: Request, db: Session = Depends(get_db)):
    """Возвращает список всех пользователей."""
    users = db.query(User).all()
    return pages.TemplateResponse("user_list.html", {"request": request, "users": users})

@app.get("/users/edit/{user_id}", response_class=HTMLResponse)
async def edit_user_form(request: Request, user_id: int, db: Session = Depends(get_db)):
    """Возвращает форму для редактирования пользователя."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден.")
    return pages.TemplateResponse("create_user.html", {"request": request, "user": user})

@app.post("/users/edit/{user_id}")
async def edit_user(user_id: int, username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    """Редактирует информацию о пользователе."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден.")
    user.username = username
    user.email = email
    user.password = password
    db.commit()
    return {"message": "Пользователь обновлён."}

@app.post("/users/delete/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    """Удаляет пользователя по ID."""
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Пользователь не найден.")
    db.delete(user)
    db.commit()
    return {"message": "Пользователь удалён."}

@app.get("/posts/create", response_class=HTMLResponse)
async def create_post_form(request: Request):
    """Возвращает форму для создания нового поста."""
    return pages.TemplateResponse("create_post.html", {"request": request})

@app.post("/posts/create")
async def create_post(title: str = Form(...), content: str = Form(...), user_id: int = Form(...), db: Session = Depends(get_db)):
    """Создаёт новый пост."""
    db_post = Post(title=title, content=content, user_id=user_id)
    db.add(db_post)
    db.commit()
    return {"message": "Пост добавлен."}

@app.get("/posts/", response_class=HTMLResponse)
async def read_posts(request: Request, db: Session = Depends(get_db)):
    """Возвращает список всех постов."""
    posts = db.query(Post).join(User).all()
    return pages.TemplateResponse("post_list.html", {"request": request, "posts": posts})

@app.get("/posts/edit/{post_id}", response_class=HTMLResponse)
async def edit_post_form(request: Request, post_id: int, db: Session = Depends(get_db)):
    """Возвращает форму для редактирования поста."""
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Пост не найден.")
    return pages.TemplateResponse("create_post.html", {"request": request, "post": post})

@app.post("/posts/edit/{post_id}")
async def edit_post(post_id: int, title: str = Form(...), content: str = Form(...), db: Session = Depends(get_db)):
    """Редактирует информацию о посте."""
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Пост не найден.")
    post.title = title
    post.content = content
    db.commit()
    return {"message": "Пост обновлён."}

@app.post("/posts/delete/{post_id}")
async def delete_post(post_id: int, db: Session = Depends(get_db)):
    """Удаляет пост по ID."""
    post = db.query(Post).filter(Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Пост не найден.")
    db.delete(post)
    db.commit()
    return {"message": "Пост удалён."}
