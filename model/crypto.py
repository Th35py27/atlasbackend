from random import randrange
from datetime import datetime
import os
import base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), unique=False, nullable=False)
    uid = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), unique=False, nullable=False)
    tokens = db.Column(db.Float, nullable=False)

    def __init__(self, name, uid, tokens, password="123qwerty"):
        self.name = name
        self.uid = uid
        self.set_password(password)
        self.tokens = tokens

    @property
    def password(self):
        return self._password[0:10] + "..."

    def set_password(self, password):
        self._password = generate_password_hash(password, "pbkdf2:sha256", salt_length=10)

    def is_password(self, password):
        return check_password_hash(self._password, password)

    def __str__(self):
        return json.dumps(self.read())

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError:
            db.session.remove()
            return None

    def read(self):
        return {
            "id": self.id,
            "name": self.name,
            "uid": self.uid,
            "tokens": self.tokens
        }

    def update(self, dictionary):
        for key in dictionary:
            if key == "name":
                self.name = dictionary[key]
            if key == "uid":
                self.uid = dictionary[key]
            if key == "password":
                self.set_password(dictionary[key])
            if key == "tokens":
                self.tokens = dictionary[key]
        db.session.commit()
        return self

    def delete(self):
        player = self
        db.session.delete(self)
        db.session.commit()
        return player


class Transaction(db.Model):
    __tablename__ = 'transactions'
    
    uid = db.Column(db.String(255), db.ForeignKey('players.uid'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    transaction_type = db.Column(db.String(50), nullable=False)

    def __init__(self, uid, amount, transaction_type):
        self.uid = uid
        self.amount = amount
        self.transaction_type = transaction_type

    def create(self):
        try:
            db.session.add(self)
            db.session.commit()
            return self
        except IntegrityError:
            db.session.remove()
            return None


def init_data():
    with app.app_context():
        db.create_all()
        
        players = [
            Player(name='Azeem Khan', uid='azeemK', tokens=45),
            Player(name='Ahad Biabani', uid='ahadB', tokens=41),
            Player(name='Akshat Parikh', uid='akshatP', tokens=40),
            Player(name='Josh Williams', uid='joshW', tokens=38),
            Player(name='John Mortensen', uid='johnM', tokens=35)
        ]

        for player in players:
            try:
                player.create()
            except IntegrityError:
                db.session.remove()
                print(f"Records exist, duplicate uid, or error: {player.uid}")

        transactions = [
            Transaction(uid='azeemK', amount=10.5, transaction_type='buy'),
            Transaction(uid='ahadB', amount=5.2, transaction_type='sell'),
            Transaction(uid='akshatP', amount=8.7, transaction_type='buy')
            # Add more transactions as needed
        ]

        for transaction in transactions:
            try:
                transaction.create()
            except IntegrityError:
                db.session.remove()
                print(f"Failed to create transaction: {transaction}")


if __name__ == "__main__":
    init_data()
