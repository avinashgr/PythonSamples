# illustrates the sets and the operations of sets
# define a set of electronic components
"""this is an example for sets and different operations on sets"""
set_of_electronics = {'calculator', 'camera', 'laptop', 'flashdrive','monitor', 'ram'}
# define a set of components used in photography
set_of_photo_equipments = {'camera', 'tripod', 'lens', 'flashdrive', 'laptop'}
# set of all components that are photo equipments but NOT electronics
set_of_non_electronic_photo = set_of_photo_equipments - set_of_electronics
# print the non electronic photo equipment
print(f'non electronic photo equipment: {set_of_non_electronic_photo}')
# set of components in both electronics and photo 
set_of_electronics_in_photo = set_of_photo_equipments & set_of_electronics
# print all electronic components in photo
print(f'all the electronic components in photography: {set_of_electronics_in_photo}')
set_of_all_equipment = set_of_electronics|set_of_photo_equipments
# print names of all the items in the store
print(f'all equipment in store: {set_of_all_equipment}')
# sort all electronic equipment in the store
print(f'sorted equipment {sorted(set_of_all_equipment)}')