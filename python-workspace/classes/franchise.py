#this is a franchise of coffee shops that manages a 
#lot of coffee shops running in different places 
#across US
import coffee_shop, store
from functools import partial

cs = coffee_shop.Coffee_Shop()

#check if cs is an instance of Store
is_cs_a_store = isinstance(cs,store.Store)
print(f'is cs an instance of store? {is_cs_a_store}')

#check if cs is an instance of Coffee_Shop
is_cs_a_coffee_shop = isinstance(cs, coffee_shop.Coffee_Shop)
print(f'is cs an instance of coffee_shop? {is_cs_a_coffee_shop}')

#invoke the functions in the Coffee_Shop class
cs.billing('MI')
cs.pay_bills()

#check if Coffee_Shop is a subclass of Store
is_cs_a_subclass = issubclass(coffee_shop.Coffee_Shop, store.Store)
print(f'the object cs is a subclass of Store? {is_cs_a_subclass}')

#add a function dynamically to instance cs
def coffee_machine(self,coffee_types):
    print(f'in store {self.__str__()} the types of coffee this machine can make {coffee_types}')

# setattr(cs, 'coffee_machine', coffee_machine)
# above works fine when self is removed from the coffee_machine def
# but the convention is to have the self in the method args as the first arg
cs.coffee_machine = partial(coffee_machine, cs)

#invoke the method and check if the coffee_machine function is part of cs instance
cs.coffee_machine(['capuccino', 'espresso', 'mocha'])

#create another instance of Coffee_Shop
cs_2 = coffee_shop.Coffee_Shop()

#check if cs_2 has the coffee_machine function
def try_coffee_machine(obj):
    try:
        obj.coffee_machine(['capuccino', 'espresso', 'mocha'])
    except AttributeError as ae:
        print(f'the error is {obj.__str__()} {ae}')

try_coffee_machine(cs_2)


#add the coffee machine method to the class Coffee_Shop
coffee_shop.Coffee_Shop.coffee_machine = coffee_machine
print(f'***added the coffee_machine function to the class Coffee_Shop ***')

#check if the instance of cs_2 is able to access the new function
try_coffee_machine(cs_2)

#check if any new instance of Coffee_Shop gets the coffee_machine
cs_3 = coffee_shop.Coffee_Shop()

try_coffee_machine(cs_3)

