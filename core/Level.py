import random
from core.Country import Country

class Level():
    def __init__(self, countries, src):
        self.countries = countries
        self.start = src
        idx = self.start
        while idx == self.start:
            idx = random.randrange(len(self.countries))
        self.dst = idx

    def run(self, time_left):
        # create country, open first window
        # options for locations     }   DONT FORGET TO
        # options for destinations  }   DECREASE TIME HERE
        # player chooses dest.
            # if dest:
                # return
            # if not dest:
                # open "not-dest window": new window that says that she wasnt here and button to go back to origin


        print("run level")

    def get_dst(self):
        return self.dst