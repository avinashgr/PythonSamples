#improves on storev1
#modularizes the routes using the blueprints
#blueprints allow using multiple files to separate 
#routes
from flask import Flask,jsonify,request

#import all blueprints from the modules of same name
#in the routes folder
from routes.menu_blueprint import menu_blueprint
from routes.store_blueprint import store_blueprint
from routes.user_blueprint import user_blueprint

app = Flask(__name__)

#register all the blueprints
app.register_blueprint(menu_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(store_blueprint)


@app.route('/')
def landing():
    return 'This is the landing page'


@app.errorhandler(Exception)
def handle_foo_exception(error):
    print('handling the error for the exception')
    return jsonify(e=str(error)), 404