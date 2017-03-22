from flask import Blueprint
from flask_restful import Api


test_blueprint = Blueprint('test', __name__)
test_blueprint_api = Api(test_blueprint)


from resource.test import TestAPI
test_blueprint_api.add_resource(TestAPI, '/test')
