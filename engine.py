"""Файл для подключения к БД"""
from sqlalchemy import create_engine

def getengine():
    """Возвращает engine для подключения"""
    engine = create_engine("sqlite:///./mydatabase.db")
    return engine
