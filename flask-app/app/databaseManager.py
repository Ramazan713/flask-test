from app.models import User
import time
from sqlalchemy import func
from app import db

class DatabaseManager:
    def __init__(self) -> None:
        pass
    def insertUser(self,name,surname):
        user=User(name,surname)
        db.session.add(user)
        db.session.commit() 

    def getAllUser(self)->list:
        users_list=[i.to_Dict() for i in User.query.all()]
        time.sleep(0.5)
        return users_list

    def getUserWithName(self,name:str):
        user=User.query.filter(func.lower(User.name)==name.lower()).all()
        if user:
            user=[i.to_Dict() for i in user]
        time.sleep(0.5)
        return user
    
    def getUserWithSurname(self,surname:str):
        user=User.query.filter(func.lower(User.surname)==surname.lower()).all()
        if user:
            user=[i.to_Dict() for i in user]
        time.sleep(0.5)
        return user
    def deleteUserWithUid(self,uid:int):
        user=User.query.filter(User.uid==uid).all()
        if user:
            db.session.delete(user[0])
            db.session.commit()
            return {"deleted users":[i.to_Dict() for i in user]}
        return {"not found":f"uid:{uid} user had been deleted or not found"}

    def deleteUserWithName(self,name:str):
        users=User.query.filter(func.lower(User.name)==name.lower()).all()
        if users:
            for user in users:
                db.session.delete(user)
            db.session.commit()
            return {"deleted users":[i.to_Dict() for i in users]}
        return {"not found":f"name:{name} user had been deleted or not found"}

    def deleteUserWithSurname(self,surname:str):
        users=User.query.filter(func.lower(User.surname)==surname.lower()).all()
        if users:
            for user in users:
                db.session.delete(user)
            db.session.commit()
            return {"deleted users":[i.to_Dict() for i in users]}
        return {"not found":f"surname:{surname} user had been deleted or not found"}
    




