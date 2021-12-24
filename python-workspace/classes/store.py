#a class that will define a store 
#basic attributes and functions that would define a store would be:
#items on the menu
#billing system
#employee payroll
#rent/lease payments
#attributes of a store - name, registration number,address, phone numbers, email, manager name
class Store:
   #stores the taxes for each state as a key value pairs
   state_taxes  = {}
   def __init__(self):
       """this is the initializer function and is reserved and is automatically called 
       when creating the object of the classS"""
       print(f'calling the function to initialize an object of type store')
   def billing(self, state):
       """calculates the final bill based on the prices and taxes"""
   def pay_bills(self):
       """pays the bills for utilities, rent and the lease agreements """
       print(f'pay bills for the store')
   def forecasted_inventory(self, period):
       """forecasts the invetory needed for the next period"""
       print(f'forecasting inventory for the store')