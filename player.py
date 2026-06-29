from coin import Coin


class Player:
    """Represents a player in the Match Coins game."""

    def __init__(self, name):
        """Initialize a player with a name, 20 coins, and one Coin object."""
        self.__name = name
        self.__wallet = 20
        self.__coin = Coin()

    def toss_coin(self):
        """Tell the player's coin to toss itself."""
        self.__coin.toss()

    def get_coin_side(self):
        """Return the current side of the player's coin."""
        return self.__coin.get_sideup()

    def win_coin(self):
        """Add one coin to the player's wallet."""
        self.__wallet += 1

    def lose_coin(self):
        """Subtract one coin from the player's wallet."""
        self.__wallet -= 1

    def get_wallet(self):
        """Return the number of coins in the player's wallet."""
        return self.__wallet

    def get_name(self):
        """Return the player's name."""
        return self.__name
