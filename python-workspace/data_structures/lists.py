#this example illustrates the lists and the manipulation of lists
#define a list of non alcoholic beverages
regular_beverages = ['coffee', 'juice', 'tea', 'milk', 'soda', 'lemonade', 'milk', 'milk','milk', 'milk']
#define a list of alcoholic beverages
alcoholic_beverages = ['vodka', 'beer', 'rum', 'margarita']
#displays the count of items in the list
print(f'the number of beverages is {len(regular_beverages)}')
#displays the number of times an item appears in the list
print(f'number of occurences of the word \'milk\': {regular_beverages.count("milk")}')
#append a duplicate word to the list
regular_beverages.append('milk')
#check if the word has been added to the original list and display
print(f'number of occurences of the word \'milk\' after appending: {regular_beverages.count("milk")}')
#all beverages
all_beverages =[]
#add alcoholic beverages
all_beverages.extend(alcoholic_beverages)
print(f'all beverages after extending to add alcoholic are: {all_beverages}')
#extend the list to add the regular beverages
all_beverages.extend(regular_beverages)
print(f'all beverages after extending to add regular are: {all_beverages}')
#find an item's first index in the list
print(f'the first index of \'milk\' is: {all_beverages.index("milk")} ')
#find all indices of word 
all_indices_of_word =[]
for i in range(all_beverages.count('milk')):
    if i == 0:
     index = all_beverages.index("milk")    
    else:
     index = all_beverages.index('milk', index+1, len(all_beverages))
    print(f'index at {index}')
    all_indices_of_word.append(index)
#remove all instances of milk from the list
print(f'length of the list of indices of \'milk\' is {len(all_indices_of_word)}')
count_of_indices = 0
while count_of_indices < len(all_indices_of_word) :
    all_beverages.remove('milk')
    count_of_indices += 1
#print the contents of all beverages without the word
print(f'the list of all beverages after the removal of \'milk\' is {all_beverages}')
#reverse the all beverage list
all_beverages.reverse()
print(f'the all beverages list after reversal is {all_beverages}')