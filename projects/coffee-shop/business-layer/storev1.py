from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/')
def landing():
    return 'This is the landing page'

#this route handles the requests for API calls for menu
#returns the menu items as in the spec for the menu GET and POST
@app.route('/menu',methods=['GET'])
def menu_get():
    print('getting the menu items for the store')
    arr_of_menuitems = [{'name':'Avinash'},{'name':'Manjula'}]    
    return jsonify(arr_of_menuitems)
#this route handles requests to add new menu item 
#returns a 200 if ok and menu item id
#returns 202 if failure
@app.route('/menu',methods=['POST'])
def menu_post():
    print('adding a menu item for the store')
    #as the request body is a json the request.json returns the json object
    item_to_add = request.json
    #check the input object for the correct format and required data
    print(f'the request from the browser is: {item_to_add}')
    arr_of_menuitems = {'id':'123456','name': 'new item','price': 5.0, 'category':'beverage' }   
    return jsonify(arr_of_menuitems)
