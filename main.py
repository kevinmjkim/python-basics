from blueWhale import BlueWhale
import random
import time



for i in range(10):
    if random.randinit(1, 10) < 3:
        print
    elif random.randint(1, 10) < 3:
        print("all pandas went extinct")

    else:
        print("they're ok for now")

    time.sleep(0.5)