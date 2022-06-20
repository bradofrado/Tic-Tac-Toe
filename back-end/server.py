from flask import Flask
from flask_restful import Resource, Api, reqparse
#import pandas as pd
#import ast

app = Flask(__name__)
api = Api(app)

class Users(Resource):
    def get(self):
        return {'data': 'hello there'}, 200  # return data and 200 OK code
    def put(self):
        return {'data': 'hello there'}, 200
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('userId', location='form')
        parser.add_argument('name', location='form')
        parser.add_argument('city', location='args')

        args = parser.parse_args()  # parse arguments to dictionary
        return {'data': args}, 200

    

api.add_resource(Users, '/users') 

if __name__ == '__main__':
    app.run()