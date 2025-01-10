from sqlalchemy import create_engine
from models import Base

# Создание подключения к базе данных
engine = create_engine('sqlite:///mydatabase.db')

# Создание всех таблиц
Base.metadata.create_all(engine)