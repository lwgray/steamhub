import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-key-for-development')
    STRAPI_URL = os.environ.get('STRAPI_URL', 'http://192.168.0.29:1337')
    STRAPI_API_TOKEN = os.environ.get('STRAPI_API_TOKEN', '')