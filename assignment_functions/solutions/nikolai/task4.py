from datetime import datetime
from time import sleep


# wrong function
def my_time_now(msg, *args, **kwargs):
    kwargs['dt']=datetime.now()
    print(msg, kwargs['dt'])

my_time_now('The time is now: ')
sleep(1)
my_time_now('The time is now: ')
sleep(1)
my_time_now('The time is now: ')