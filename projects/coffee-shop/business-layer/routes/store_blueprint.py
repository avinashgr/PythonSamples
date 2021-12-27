#blueprint for the routes for the Store API
from flask import Flask,jsonify,request, Blueprint

store_blueprint = Blueprint('store_blueprint', __name__)

@store_blueprint.route('/menu')
def index():
    return "This is an example app"
