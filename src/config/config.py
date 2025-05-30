from decouple import config

class Config:
    SECRET_KEY = config('SECRET_KEY')
    TWILIO_ACCOUNT_SID = config('TWILIO_ACCOUNT_SID')
    TWILIO_AUTH_TOKEN = config('TWILIO_AUTH_TOKEN')
    TWILIO_WHATSAPP_NUMBER = config('TWILIO_WHATSAPP_NUMBER')

class DevelopmentConfig(Config):
    DEBUG: True

app_config = {
    'development': DevelopmentConfig
}
