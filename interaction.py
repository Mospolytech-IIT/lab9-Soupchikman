from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

user1 = User(username='user', email='user@gmail.com', password='password')
user2 = User(username='Oleg', email='oleja@yandex.ru', password='nobodyknow')

session.add(user1)
session.add(user2)

post1 = Post(title='Post', content='Content1', user=user1)
post12 = Post(title='Post2', content='Content2', user=user1)
post2 = Post(title='Post of SpokTuber', content='ContentWarning', user=user2)

session.add(post1)
session.add(post12)
session.add(post2)

session.commit()

def getdata(session):
    users = session.query(User).all()

    for user in users:
        print(user.username, user.email)

    posts = session.query(Post).all()

    for post in posts:
        print(post.title, post.content, post.user.username)

    user_posts = session.query(Post).filter_by(user_id=user1.id).all()
    for post in user_posts:
        print(post.title, post.content)
        
def updatedata(session):
    user1.email = 'ultra@gmail.com'
    #session.commit()
    post12.content = 'ULTRA Mega New CONTENT!!!'
    session.commit()

def deletedata(session):
    session.delete(post1)
    #session.commit()
    session.delete(user2)
    posts_to_delete = session.query(Post).filter_by(user=user2).all()
    for post in posts_to_delete:
        session.delete(post)
    session.commit()

if __name__ == "__main__":
    engine = create_engine('sqlite:///database.db')
    Session = sessionmaker(bind=engine)
    my_session = Session()

    add_data(my_session)
    get_data(my_session)
    update_data(my_session)
    delete_data(my_session)


















    
