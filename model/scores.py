from random import randrange
from datetime import datetime
import os
import base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash

class Score(db.Model):
    __tablename__ = 'scores'
    score_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    #transaction_id = db.Column(db.Float,primary_key=True)
    user_id = db.Column(db.Float, db.ForeignKey('users.id'), nullable=False)
    #amount = db.Column(db.Float, nullable=False)
    #transaction_type = db.Column(db.String(50), nullable=False)
    #executed_price = db.Column(db.Float, nullable=False)
    score = db.Column(db.Float, nullable=False)



    #def __init__(self,user_id, amount, transaction_type,executed_price):
    def __init__(self,user_id, score):
        self.user_id = user_id
        self.score = score
        #self.transaction_type = transaction_type
        #self.executed_price = executed_price
    

    def create(self):
        try:
            print(self.user_id)
            print(self.score)
            print("inside model")

            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError:
            db.session.remove()
            return None



#if __name__ == "__main__":
    #init_data()
