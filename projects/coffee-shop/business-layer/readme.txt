server side component that performs the following
1. responds to the first request with an index.html
2. has the following endpoints:

Menu API:
--------
POST /menu - adds items to the menu
GET /menu/{item} -gets the info for an item in the menu
GET /menu - gets all items in the menu
DELETE /menu/{item}- deletes a specified item in the menu 

Store API:
-----------
POST /store/oder - posts the order to the store
GET /store/inventory - gets the inventory in the store
GET /store/order/{orderid} - gets the order information from the order inde
DELETE /store/order/{orderid} - deletes the order based on the order id

Authentication API:
------------------
POST /authenticate

Steps to create the project folder
----------------------------------
cd ~/business-layer

#create a virtualenv for the project as below:
------------------------------------------------
python3 -m venv venv 
code .

When visual studio code opens in the directory "business-layer"
1. Go to View> Command Palette or use the shortcut keys CNTRL+SHIFT+P
2. Type Python: Select Interpreter
3. Choose the python in the ./venv/bin/python3
4. Open the terminal and it should display the folder as inside the venv virtualenv

create the project specific folders and files
---------------------------------------------
mkdir -p app/templates app/static
touch store.py
touch config.py
touch app/

install and Flask inside the venv
---------------------------------
pip install flask

check if the flask package is intalled in the local env
--------------------------------------------------------
pip list --local

result:
-------
Package       Version
------------- -------
click         8.0.3  
Flask         2.0.2  
itsdangerous  2.0.1  
Jinja2        3.0.3  
MarkupSafe    2.0.1  
pip           20.0.2 
pkg-resources 0.0.0  
setuptools    44.0.0 
Werkzeug      2.0.2  

in VSCode reload Developer Window using : CNTRL+SHIFT+P and then Developer: Reload Window
this will reload the python workspace with any of the updated pip modules added to the venv


