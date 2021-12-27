#blueprint for the routes for the User API
from flask import Flask,jsonify,request, Blueprint

user_blueprint = Blueprint('user_blueprint', __name__)

@user_blueprint.route('/menu')
def index():
    return "This is an example app"
