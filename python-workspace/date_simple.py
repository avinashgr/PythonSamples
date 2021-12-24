from datetime import datetime, timedelta
import calendar

#get current date
today_date = datetime.now();
#print the date as a string
print('the date today is '+str(today_date))
print_date = f'today the date is {today_date}'
print(print_date)

#print the date one week before today
days = timedelta(days=16)
week_back = today_date - days
print('the date 1 week back from today is: '+str())
print(' the weekday 16 days from today: {0}'.format(calendar.day_name[week_back.weekday()]))

#enhance this code to do the following:
# get the date from user
# get the days to backdate
# display message with days 
# ex: if the user wanted to see 10 days back then the message needs to reflect the weekday 10 days back from selected date is : Monday