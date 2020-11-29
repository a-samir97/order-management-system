from flask import Flask
from dotenv import load_dotenv


import models
import os

load_dotenv()

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY=os.getenv('SECRET_KEY'),
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://%s:%s@%s:%s/%s' % 
    (
        os.getenv("DB_USERNAME"), 
        os.getenv("DB_PASSWORD"),
        os.getenv("DB_HOST"),
        os.getenv("DB_PORT"),
        os.getenv("DB_NAME")
    ),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
))

models.init_app(app)
models.create_tables(app)

if __name__=='__main__':
    app.run(debug=True)