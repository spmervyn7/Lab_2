import random


class Coin:
    """Represents a single coin that can be tossed."""

    def __init__(self):
        """Initialize the coin with a random side facing up."""
        self.__sideup = random.choice(["Heads", "Tails"])

    def toss(self):
        """Randomly set the coin side to Heads or Tails."""
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        """Return the current side facing up."""
        return self.__sideup