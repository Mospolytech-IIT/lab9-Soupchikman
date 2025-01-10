from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Post

engine = create_engine('sqlite:///mydatabase.db')
Session = sessionmaker(bind=engine)
session = Session()

user1 = User(username="Николай", email="kolyamesh@yandex.com", password="parol")
user2 = User(username="Dvinyatin", email="dvin2@yandex.com", password="serso")

session.add(user1)
session.add(user2)
session.commit()

post11 = Post(title="Что?", content="И что это в ящике такое?", user_id=user1.id)
post12 = Post(title="Где?", content="Где располагаемся мы?", user_id=user1.id)
post13 = Post(title="Когда?", content="Когда муха села на Пушкина...", user_id=user1.id)
post2 = Post(title="SersoProblem", content="А как же серсо?!", user_id=user2.id)

session.add(post11)
session.add(post12)
session.add(post13)
session.add(post2)
session.commit()
