#this is example of all the things we have learnt so far in the
#the basics of python
#it shows the following:
#lists, sets, functions, modules, comprehesion statements
#logical seperation, file reading, JSON format and parsing JSON
#modules in packages
from  util_modules.inventory import categorize, calculate_bill
#starting a coffee shop is not easy. You need stuff and lots of it!
#electronics, furniture, lights, coffee machine, building material
#if you want the user to enter the items in the commandline then "coffee_shop.py ipad paint"
if __name__ == "__main__":
    import sys
    items_to_categorize = sys.argv[1:]
if len(items_to_categorize) == 0:
    items_to_categorize = ['ipad', 'blender', 'paint', 'table', 'shelf', 'bulb', 'flowerpot']
print(f'\nitems to categorize are: {items_to_categorize}')
items_categorized  = categorize(items_to_categorize)
#you need a billing system that can lookup the prices of items and then
#bill a customer fast considering the location, price and taxes
print(f'\nthe categories are {items_categorized}')
receipt = calculate_bill(['espresso','muffin','iced_tea'], 'california')
print(f'the receipt will be ${receipt}')
