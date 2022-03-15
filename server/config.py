import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


ENV = os.environ.get("FLASK_ENV", default="production")
DEBUG = ENV == "development"
SECRET_KEY = os.environ.get("SECRET_KEY", default="super-secret")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")