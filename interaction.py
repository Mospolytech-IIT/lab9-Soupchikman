from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Post
from engine import getengine

def addata(session):
    user1 = User(username='user', email='user@gmail.com', password='password')
    user2 = User(username='Oleg', email='oleja@yandex.ru', password='nobodyknow')
    session.add_all([user1, user2])
    session.commit()

    post1 = Post(title='Post', content='Content1', user_id=user1.id)
    post12 = Post(title='Post2', content='Content2', userid=user1.id)
    post2 = Post(title='Post of SpokTuber', content='ContentWarning', userid=user2.id)
    session.add_all([post1, post12, post2])
    session.commit()

def get_data(session):
    users = session.query(User).all()

    for user in users:
        print(user.username, user.email)

    posts = session.query(Post).all()

    for post in posts:
        print(post.title, post.content)

    user_posts = session.query(Post).filter_by(userid=user1.id).all()
    for post in user_posts:
        print(post.title, post.content)
        
def updatedata(session):
    user1.email = 'ultra@gmail.com'
    session.commit()
    post12.content = 'ULTRA Mega New CONTENT!!!'
    session.commit()

def deletedata(session):
    session.delete(post1)
    session.commit()
    posts_to_delete = session.query(Post).filter_by(userid=user2.id).all()
    for post in posts_to_delete:
        session.delete(post)
    session.delete(user2)    
    session.commit()

if __name__ == "__main__":
    engine = getengine()
    Session = sessionmaker(bind=engine)
    mysession = Session()

    addata(mysession)
    getdata(mysession)
    updatedata(mysession)
    deletedata(mysession)

    mysession.close()


















    
