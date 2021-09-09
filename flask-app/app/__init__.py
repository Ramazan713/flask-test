from flask import Flask
from flask_caching import Cache
from config import getConfig
from flask_sqlalchemy import SQLAlchemy
import os,logging

app_dir=os.path.dirname(os.path.realpath(__file__))
log_config_file=os.path.join(os.path.abspath(f"{app_dir}/.."),"log_config.yml")

config_obj=getConfig()

app=Flask(__name__)
app.config.from_object(config_obj)

cache=Cache(app)
db=SQLAlchemy(app)

def logmaker():
    log_path=f"{app_dir}/{config_obj.LOG_FILENAME}"
    return logging.FileHandler(log_path,mode=config_obj.LOG_FILE_MOD)



from app import databaseManager
dbManager=databaseManager.DatabaseManager()
from app import views




db.create_all()
