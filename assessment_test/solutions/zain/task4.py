from datetime import datetime
from time import sleep
 
def my_time_now(msg, *, dt=None):
    if dt==None:
        dt=datetime.now()
    print(msg, dt)
# simple tests :)
my_time_now('The time is now: ')
sleep(1)
my_time_now('The time is now: ')
sleep(1)
my_time_now('The time is now: ')