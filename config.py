import os 

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    #SQLALCHEMY_DATABASE_URI = " SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:test123@localhost/blogger""
    UPLOADED_PHOTOS_DEST = "app/static/photos"

    # email configurations
    MAIL_SERVER = "smtp.gmail.com"
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = postgresql://caqifpdubxufnz:'84e3fd6a327f4cb5db1f87106fe78ace435b8858cd1c554974c746dac81a2f3c@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d7v5ctmoa02fph?sslmode=require'

class TestConfig(Config):
    
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:test123@localhost/blogger_test"

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:test123@localhost/blogger"
    DEBUG = True


config_options = {
    "development": DevConfig,
    "production": ProdConfig,
    "test": TestConfig
}