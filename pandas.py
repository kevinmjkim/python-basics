import time
import random


class Pandas:
    for i in range(10):
        if random.randint(1, 10) < 3:
            print("all pandas went extinct")
            exit()
        else:
            print("they're ok for now")

        time.sleep(0.5)

    def __init__(self, is_it_a_boy, height, weight):
        self.is_it_a_boy = is_it_a_boy
        self.height = height
        self.weight = weight



    def check_weight(self):
        return self.weight

    def check_height(self):
        return self.height

    def eat_bamboo(self):
        print("om nom")
        self.weight += 100
        self.height += 5

    def try_not_to_go_extinct(self):
        for i in range(10):
            if random.randint(1, 10) < 3:
                print("Oh no will they die?")
                if random.randint(1, 2) == 2:
                    print("They survived!")
                else:
                    print("Pandas went extinct!")
                exit()


            else:
                print("they're ok for now")

        time.sleep(0.5)

    def poop(self):
        if self.weight > 50:
            print("<poop noise>")
            self.weight -= 25
        else:
            print("oops! the whale died")
            self.weight = 0
