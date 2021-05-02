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
    
    SQLALCHEMY_DATABASE_URI = "postgresql://wdufijrivdzeof:8cc7c0cc28562357dc250002f1cdbd8852cc07378be8b06331129e8224d17ca4@ec2-52-7-115-250.compute-1.amazonaws.com:5432/d1tiq4quv8fgd1?sslmode=require"
  #SQLALCHEMY_DATABASE_URI  =os.environ.get("DATABASE_URL") 
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