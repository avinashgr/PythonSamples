# compreshensions are used to create lists in a concise way
# the creation statement is readable and uses a logical statement to
# create the list
# long form creation
"""This program illustrates the concise creation of lists"""
# create a list of all beverages that have non alcoholic (na_) and alcoholic beverages (a_)
all_beverages = ['a_vodka','a_beer', 'a_margarita', 'a_seltzer', 'a_rum',
'na_hot_chocolate','na_orange_juice', 'na_coffee', 'na_tea']
#get beverages that are have na_ in the prefix
non_alcoholic_bevs = [bev for bev in all_beverages if 'na_' in bev ]
print(f'non alcoholic beverages filtered as {non_alcoholic_bevs}')

#same example in long form code
non_alcoholic_bevs.clear()
for bev in all_beverages:
    if 'na_' in bev:
        non_alcoholic_bevs.append(bev)

print(f'non alcoholic beverages filtered as {non_alcoholic_bevs}')