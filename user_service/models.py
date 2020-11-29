from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from passlib.hash import sha256_crypt


db = SQLAlchemy()

def init_app(app):
    db.app = app
    db.init_app(app)
    return db


def create_tables(app):
    engine = create_engine(app.config["SQLALCHEMY_DATABASE_URI"])
    db.metadata.create_all(engine)
    return engine


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    first_name = db.Column(db.String(255), nullable=True)
    last_name = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, onupdate=datetime.utcnow)

    def __str__(self):
        return self.username

    def encrypt_password(self):
        self.password = sha256_crypt.hash(self.password)
    
    def is_authenticated(self):
        return self.authenticated
    
    def get_username(self):
        return self.username

    def get_id(self):
        return self.id
    
    def to_json(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "username": self.username,
            "email": self.email
        }