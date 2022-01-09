#blueprint for the routes for the Menu API
from flask import Flask,jsonify,request, Blueprint,abort

import uuid

menu_blueprint = Blueprint('menu_blueprint', __name__)

#global list of menu items
#pictures from : https://www.thephotoargus.com/images-of-coffee/
list_of_menuitems = [{'id':'1234','name': 'espresso','price': 5.0, 'picture': 'https://www.thephotoargus.com/wp-content/uploads/2019/05/latte.jpg', 'category':'beverage' },
    {'id':'5678','name': 'mocha latte','price': 3.50, 'picture': 'https://www.thephotoargus.com/wp-content/uploads/2019/05/coffeephotography01.jpg','category':'beverage' },
    {'id':'9012','name': 'cappuccino','price': 6.0,'picture': 'https://www.thephotoargus.com/wp-content/uploads/2019/05/coffeephotography05.jpg','category':'beverage' },
    {'id':'3456','name': 'chai latte','price': 7.0,'picture': 'https://www.thephotoargus.com/wp-content/uploads/2019/05/coffeephotography13.jpg','category':'beverage' },
    {'id':'7890','name': 'Dark Roasted Espresso','price': 7.0,'picture': 'https://www.thephotoargus.com/wp-content/uploads/2019/05/coffeephotography11.jpg','category':'beverage' }]
#this route handles the requests for API calls for menu
#returns the menu items as in the spec for the menu GET and POST
@menu_blueprint.route('/menu',methods=['GET'])
def menu_get():
    global list_of_menuitems
    print('getting the menu items for the store')
    arr_of_menuitems = list_of_menuitems    
    return jsonify(arr_of_menuitems)
#this route handles requests to add new menu item 
#returns a 200 if ok and menu item id
#returns 202 if failure
@menu_blueprint.route('/menu',methods=['POST'])
def menu_post():
    print('adding a menu item for the store')
    #as the request body is a json the request.json returns the json object
    item_to_add = request.json
    #check the input object for the correct format and required data
    print(f'the request from the browser is: {item_to_add}')
    item_to_add['id']= uuid.uuid4().hex[:8]
    list_of_menuitems.append(item_to_add)
    return jsonify(item_to_add)

@menu_blueprint.route('/menu/<menuitem>',methods=['GET'])
def menu_item_get(menuitem=None):
    print(f'the menuitem in the request is {menuitem}')
    #check if the menuitem is found in the system
    #if the menuitem is found then return in reponse
    menu_item_info = {'id':'123456','name': 'new item','price': 5.0, 'category':'beverage' }   
    if(menuitem == '12345'):
     return jsonify(menu_item_info)
    else:
        # return "not found", 404
        abort(404, description="Resource not found")

@menu_blueprint.route('/menu/<menuitem>',methods=['DELETE'])
def menu_item_delete(menuitem=None):
    print(f'the menuitem in the request is {menuitem}')
    global list_of_menuitems
    if(menuitem):
      items = [i for i in list_of_menuitems if i['id'] != menuitem]
      list_of_menuitems = items
      return  jsonify(success=True)
    else:
        # return "not found", 404
        abort(404, description="Resource not found")