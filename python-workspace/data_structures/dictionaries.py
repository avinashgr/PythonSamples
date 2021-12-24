#this is an example of dictionaries
# dictionaries are used to store key and value pairs
# keys have to be unique and value can be any sring 
"""this is an example of how to use dictionaries"""
# let's create a disctionary of different types of stores 
# and assign them keys to uniquely codify them
dict_of_stores = {'store_1': 'coffee',
'store_2':'bakery', 'store_3':'groceries', 'store_4':'electronics'}
try:
   print (' the value of store_1 is ', dict_of_stores['store_1'])

   print (' the value of store_1 is ', dict_of_stores['store_3'])

   print (' the value of the store_6 is ', dict_of_stores['store_6'])
except KeyError as e:
    print (f' No such key {e}')