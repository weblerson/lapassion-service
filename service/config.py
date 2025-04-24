from decouple import config


class Config:
    HOST = config('HOST', cast=str)
    PORT = config('PORT', cast=int)
    DEBUG = config('DEBUG', cast=bool)
