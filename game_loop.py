from player import Player


def print_wallets(player1, player2):
    """Print both players' current wallet totals."""
    print(f"{player1.get_name()} has {player1.get_wallet()} coins.")
    print(f"{player2.get_name()} has {player2.get_wallet()} coins.")


def print_final_results(player1, player2):
    """Print the final score and winner."""
    print("\n--- Final Score ---")
    print(f"{player1.get_name()}: {player1.get_wallet()}")
    print(f"{player2.get_name()}: {player2.get_wallet()}")

    if player1.get_wallet() > player2.get_wallet():
        print(f"{player1.get_name()} finished with more coins!")
    elif player2.get_wallet() > player1.get_wallet():
        print(f"{player2.get_name()} finished with more coins!")
    else:
        print("It's a draw!")


def main():
    """Create the players and run the game loop."""
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    print("--- Coin Match Game ---")
    print_wallets(player1, player2)

    play_again = input("\nDo you want to toss the coins? (y/n): ")

    while play_again == "y" or play_again == "Y":
        print("\nTossing...")

        player1.toss_coin()
        player2.toss_coin()

        side1 = player1.get_coin_side()
        side2 = player2.get_coin_side()

        print(f"{player1.get_name()} tossed {side1}")
        print(f"{player2.get_name()} tossed {side2}")

        if side1 == side2:
            player1.win_coin()
            player2.lose_coin()
            print(f"...It's a Match! {player1.get_name()} wins a coin.")
        else:
            player2.win_coin()
            player1.lose_coin()
            print(f"...No Match! {player2.get_name()} wins a coin.")

        print()
        print_wallets(player1, player2)

        if player1.get_wallet() == 0 or player2.get_wallet() == 0:
            print("\nGame over! A player has run out of coins.")
            break

        play_again = input("\nDo you want to toss the coins? (y/n): ")

    print_final_results(player1, player2)

if __name__ == "__main__":
    main()