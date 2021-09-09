import os

db_user=os.environ.get("DB_USER")
db_password=os.environ.get("DB_PASSWORD")
db_host=os.environ.get("DB_HOST")
db_database_name=os.environ.get("DB_DATABASE")

redis_host=os.environ.get("REDIS_HOST")
redis_port=os.environ.get("REDIS_PORT")
redis_password=os.environ.get("REDIS_PASSWORD")

class Config:
    SERVER_PORT=5000
    DEBUG=False
    HOST="0.0.0.0"
    FLASK_ENV = "production"
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    CACHE_TIMEOUT=10
    LOG_FILE_MOD="w"
    LOG_FILENAME="logs/app.log"

class ProductionConfig(Config):
    DEBUG=False
    SQLALCHEMY_DATABASE_URI=f"postgresql://{db_user}:{db_password}@{db_host}/{db_database_name}"#mysql+mysqlconnector postgresql
    CACHE_TYPE="RedisCache"
    CACHE_REDIS_HOST=redis_host
    CACHE_REDIS_PORT=redis_port
    CACHE_REDIS_PASSWORD=redis_password

class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI="postgresql://postgres:123456789@localhost/dtx"
    CACHE_TYPE="RedisCache"
    CACHE_REDIS_HOST="localhost"
    CACHE_REDIS_PORT=6379
    CACHE_REDIS_PASSWORD=""
    DEBUG=True
    TESTING=True
    

def getConfig():
    if Config.FLASK_ENV=="production":
        return ProductionConfig()
    else:#development
        return DevelopmentConfig()
