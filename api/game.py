import json
import random

from flask import Flask, Blueprint, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime
from auth_middleware import token_required
from model.scores import Score
from model.users import User
from __init__ import db, app
import sqlite3

game_api = Blueprint('game_api', __name__, url_prefix='/api/game')
api = Api(game_api)
dbURI = './instance/volumes/sqlite.db'

class Connections:
    class PointSystem(Resource):
        def post(self):
            try:
                body = request.get_json()
                uid = body.get('uid')
                score = int(body.get('score'))
                con = sqlite3.connect(dbURI)
                cur = con.cursor()
                print(uid)
                print(score)
                user = User.query.filter_by(_uid=uid).first()
                print("Before score")
                points = Score(uid, score)
                print("After score")
                points.create()
            except Exception as e:
                return {'message': 'Something went wrong', 'error': str(e)}

    api.add_resource(PointSystem, '/score')
