# illustrates creation of queues ("FIFO"- first in first out)
# first in first out is where the item that has been inserted first is the first to
# be processed
from collections import deque
# define a queue of pizza orders
list_of_orders = [
    'John - order for 1 pizza ',
    'Sam - order for wings',
    'Dave - order for bread sticks',
    'Bob - order for salad'  ]


def process_orders(list_of_orders):
    """function to process orders as queue"""
    queue = deque(list_of_orders)
    for i in range(len(list_of_orders)):
        print(f'processing {queue.pop()}')

def add_orders_to_left(list_of_orders, list_to_add):
    """function to process orders as queue"""
    queue = deque(list_of_orders)
    queue.extendleft(list_to_add)
    return list(queue)


premium_orders = ['Jimmy - order for salad and wings', 'Jack - order of square pizza']

list_of_orders = add_orders_to_left(list_of_orders,premium_orders)

process_orders(list_of_orders)
