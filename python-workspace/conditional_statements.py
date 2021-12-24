#demo to show conditional statements
#user enters his date of birth
#program calculates the age and tells if he eligible for a driver's permit

from datetime import datetime
from dateutil import relativedelta

#adding a try catch to handle errors in the input date
try:
    i_date_of_birth = input('enter your date of birth (mm/dd/yyyy): ')
    print(f'the date of birth entered: {i_date_of_birth}')
    #convert the input date to date
    date_of_birth = datetime.strptime(i_date_of_birth, '%m/%d/%Y')
except ValueError:
    raise ValueError(f'incorrect date entered as: {i_date_of_birth}')

#find the difference between the current date and input DOB
diff  = datetime.now()-date_of_birth
print(f'the difference in days {diff.days}')

#what we need is the difference in years and years can have leap years
#months may be long and short in cases where we need difference in days, months and weeks
#the relativedelta module from the dateutil provides the handy util function that does this
diff_in_years = relativedelta.relativedelta(datetime.now(),date_of_birth)
print(f'age in years {diff_in_years.years} years and {diff_in_years.months} months')

#logic to check if eligible for driver's license
if diff_in_years.years > 17 :
    print('Eligible for the driver\'s license')
else:
    print('Not eligible for the driver\'s license')