
import json
from app import db


class User(db.Model):
    __tablename__="users"
    uid=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    surname=db.Column(db.Text)

    def __init__(self,name,surname,uid=None) -> None:
        super().__init__()
        self.name=name
        self.surname=surname
        if uid:
            self.uid=uid
    def __repr__(self) -> str:
        return json.dumps({colName.name:getattr(self,colName.name) for colName in self.__table__.columns})
    def to_Dict(self):
        return {colName.name:getattr(self,colName.name) for colName in self.__table__.columns}

    