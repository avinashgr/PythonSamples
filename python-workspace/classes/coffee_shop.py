#extends the concept of a store 
#to a coffee shop
import store

class Coffee_Shop(store.Store):


       def billing(self, state):
        """calculates the final bill based on the prices and taxes"""
        print(f'items purchased in {state}')
