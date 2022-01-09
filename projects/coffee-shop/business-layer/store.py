#improves on storev1
#modularizes the routes using the blueprints
#blueprints allow using multiple files to separate 
#routes
from flask import Flask,jsonify,request

#for all the post requests an OPTION requests needs to be supported
#ref:https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS
from flask_cors import CORS

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
CORS(menu_blueprint)

@app.route('/')
def landing():
    return 'This is the landing page'


@app.errorhandler(Exception)
def handle_foo_exception(error):
    print('handling the error for the exception')
    return jsonify(e=str(error)), 404

#adds the headers that common to all requests    
@app.after_request
def do_something_whenever_a_request_has_been_handled(response):
    # we have a response to manipulate, always return one
    #if the header is not added then the browser will not process the response
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Methods', '*')
    response.headers.add('Access-Control-Allow-Headers', '*')
    return response