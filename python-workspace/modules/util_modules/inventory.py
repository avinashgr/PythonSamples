# the inventory module provides the inventory managment
# functions needed to check the inventory
# categorize the inventory
# sort inventory by the number of items
import json
from pathlib import Path


list_of_electronics = ['calculator', 'monitor','flashdrive', 'samrtphone', 'ipad']
list_of_furniture = ['table', 'chair', 'shelf', 'couch', 'paint']
list_of_kitchen_items = ['spoon', 'knife', 'pan', 'blender']
list_of_electricals = ['bulb', 'fan', 'plug', 'socket']

coffee_menu = {'mocha': 7.00,
'espresso': 5.00,
'americano': 5.00,
'latte': 6.00,
'muffin': 3.00,
'hot_tea': 3.00,
'iced_tea': 3.25}

state_taxes = Path('./state_taxes.json').read_text()

def categorize(items):
    """this function gets items and categorizes them into sets"""
    electronics = {e for e in items if e in list_of_electronics }
    kitchen = {k for k in items if k in list_of_kitchen_items}
    furniture = {f for f in items if f in list_of_furniture}
    electricals = {el for el in items if el in list_of_electricals}
    miscellaneous = set(items) - (electronics| kitchen | furniture | electricals)
    return {'electronics':list(electronics),
    'kitchen': list(kitchen),
    'furniture': list(furniture),
    'electricals': list(electricals),
    'miscellaneous':list(miscellaneous)}

def calculate_bill(purchased_items, state):
    """This functions calculates the bill based on items purchased, tax and state"""
    # load taxes from in the json format from file contents already loaded
    state_taxes_as_json = json.loads(state_taxes)
    # print(f'the json in the file was found as {state_taxes_as_json}')
    state_info = [tax for tax in state_taxes_as_json if tax['State'].lower() == state.lower()]
    #get the first item and store the tax rate
    tax_rate = state_info[0]["stateTaxRate"]
    print(f'sales tax rate for {state} is {tax_rate} %')
    #calculate the bill based on the state and the itm
    bill = 0.0
    for item in purchased_items:
        bill = bill + coffee_menu[item] + float(tax_rate)/100 * coffee_menu[item]

    print(f'receipt for the customer purchase is: {bill}')
    return bill