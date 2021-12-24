#takes the driver's license example and adds functions
#most of the logic needed can be grouped as functions
#functions 
# 1.improve readability
# 2.can be exported and reused
# 3.easier for debugging
# 4.logical grouping that can be modified independently of other logic
#prompts user to enter the correct date before moving on to checks
from datetime import datetime
#function to get the date of birth from a user
def getUserDOB():
    #1.get the user's age
        i_date_of_birth = input('enter your date of birth (mm/dd/yyyy): ')
        print(f'the date of birth entered: {i_date_of_birth}')
    # #2.1 check for empty
    #     is_str  = isinstance(i_date_of_birth, str)
    #     if is_str is False:
    #         print(f'the date is empty')
    #         raise ValueError; 
    #2.1 check for spaces and trim leading and ending spaces
        i_date_of_birth = i_date_of_birth.strip()
    #2.2 check for correct format
        datetime.strptime(i_date_of_birth, '%m/%d/%Y')
        print("This is the correct date string format.")
        return i_date_of_birth
#loop till the user enters a valid date for DOB
def loopForDate():
    check_date_valid = False
    while check_date_valid is False:
        i_date_of_birth = str
        try:
            i_date_of_birth = getUserDOB()
            break
        except ValueError:
            print(f'incorrect date entered as: {i_date_of_birth}')
            continue
    return i_date_of_birth

i_date_of_birth = loopForDate()

#3.if yes store date and continue to 4 and if not go back to 1
print(f'the date entered: {i_date_of_birth} is valid')
#4.logic for year check and driver's license eligibility