from flask import jsonify
from flask_restful import Resource

class TestAPI(Resource):
    def get(self):
        return 'hello world'