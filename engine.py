"""Файл для подключения к БД"""
from sqlalchemy import create_engine

def getengine():
    """Возвращает engine для подключения"""
    engine = create_engine("sqlite:///./database.db")
    return engine
