

from datetime import datetime
from time import sleep

def my_time_now(msg, *, dt=None):
    if dt is None:
        dt = datetime.now()  #
    print(msg, dt)

my_time_now('The time is now: ')
sleep(5)
my_time_now('The time is now: ')
sleep(5)
my_time_now('The time is now: ')


