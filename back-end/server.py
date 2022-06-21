from flask import Flask
from flask_restful import Resource, Api, reqparse
#import pandas as pd
#import ast

app = Flask(__name__)
api = Api(app)

class MiniMax(Resource):
    def post(self):
        parser = reqparse.RequestParser()  # initialize
        parser.add_argument('board', location='form')
        
        args = parser.parse_args()  # parse arguments to dictionary
        return {'data': args}, 200  # return data and 200 OK code

    

api.add_resource(MiniMax, '/api/minimax') 

if __name__ == '__main__':
    app.run()