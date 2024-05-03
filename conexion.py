from sqlalchemy import create_engine

DATABASE_URL = "sqlite:///-/test.db" # ejemplo de conexion a SQLite

engine = create_engine(DATABASE_URL)