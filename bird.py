class Bird:
    def __init__(self, am_i_a_boy):
        self.am_i_a_boy = am_i_a_boy

    def make_noise(self):
        if self.am_i_a_boy:
            print("*sings an entire song*")
        else:
            print("chirp chirp")
        # eats

    def eat(self):
        if self.am_i_a_boy:
            print("poke poke poke eat eat eat")
        else:
            print("*swallows*")

        # poops

    def poop(self):
        if self.am_i_a_boy:
            print("*nuclear bomb noises*")
        else:
            print("*drip*")
        # sleeps

    def sleep(self):
        if self.am_i_a_boy:
            print("*silence*")
        else:
            print("*silence*")