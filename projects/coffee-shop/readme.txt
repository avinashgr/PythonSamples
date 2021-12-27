Components coffee-shop website
---------------------------------
web-ui: single page web app, a client for the coffee shop owner and the customers to use for online/instore 

Customer View
-------------
view menu
order items

Admin View
----------
Add items to menu

business-layer - server side business logic for authentication, business logic and persistence

Design
------
1. web-ui is a single page app built in JQuery, HTML, CSS 
2. business-layer is a python app built with Flask as the http framework managing the routes
3. ReSTful API: api used to transmit data between ui and business layer
4. JSON: payload format used for data transfer between layers

Implementation
--------------
1. install virtual environment
   cd business-layer
   virtualenv venv
2. install Flask
   pip install flask



