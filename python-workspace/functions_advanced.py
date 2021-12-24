#this example illustrates the different ways functions can be defined and used
#default values in argument list
def coffee_or_tea(prompt, retries=4, reminder='We only have coffee or tea'):
    """function gathers the input and allows user to pick options"""
    while True:
        beverage = input(prompt).lower().strip() 
        if beverage in ['coffee', 'tea']:
            print(f'Please wait. We are getting your {beverage} ready')
            return True
        else:
            retries = retries -1
            print(f'{reminder}')
        if retries < 0:
            print('Sorry, we tried. Please come back another day!')
            break

def get_the_menu(request,*responses, **menuitems):
    """gets the menu and displays the menu when user inputs menu"""
    while True:
        i_type = input(request).lower().strip()
        if i_type == 'menu':
            for resp in responses:
                print(f'{resp}')
                print(f'here is the menu for today: ')
            for item in menuitems.items():
                print (f'for {item}, we have {menuitems[item]}')
                break
        else:
            print ('I can get you our menu')
            continue

# invoke function with no param, remember no default value specified for prompt
# coffee_or_tea()
# invoke with prompt only
# coffee_or_tea("What can we get for you?")
# invoke with retries set to 2
# coffee_or_tea('What can we get for you today? We have coffee or tea', retries=2)
# coffee_or_tea('What can I get for you?', reminder='we have coffee and tea.. your choice')

get_the_menu('what can I get for you today',
'hope you are having a great day',
'the weather is so nice today',
lunch=['eggs and bacon', 'shrimp scampi'],
breakfast='ham sandwich'
)