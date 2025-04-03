from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG: True

app_config = {
    'development': DevelopmentConfig
}
