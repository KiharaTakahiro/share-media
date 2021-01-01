import sqlalchemy
from app.db import metadata, engine

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, index=True),
    sqlalchemy.Column("username", sqlalchemy.String, index=True),
    sqlalchemy.Column("email", sqlalchemy.String, index=True),
    sqlalchemy.Column("password", sqlalchemy.String),
    sqlalchemy.Column("age", sqlalchemy.Integer),
)

metadata.create_all(bind=engine)