first_name  = input('What is the first name? ')
last_name = input('What is the last name? ')
print('the full name is '+first_name+' '+last_name)
#print the capitalized first and last names
print('capitalized first name '+ first_name.capitalize())
print('capitalized last name '+ last_name.capitalize() )
#print concatenated first and last name
print('the full name capitalized is '+first_name.capitalize()+' '+last_name.capitalize())
#print count of the total letters in full name
print('the count of all letters in full name ')
print((first_name+last_name).count("a"))
#print simplify with format
print('Hello {0} {1}'.format(last_name, first_name))
#only in python3
output = f'Hello {first_name} {last_name}'
print(output)