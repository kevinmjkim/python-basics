from blueWhale import BlueWhale
from pandas import Pandas
import random
import time



for i in range(10):
    if random.randint(1, 10) < 3:
        print("all pandas went extinct")
        exit()
    else:
        print("they're ok for now")

    time.sleep(0.5)
