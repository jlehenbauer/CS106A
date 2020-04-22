
def main():
    """
    Hosts a game of Nimm to be played by two players.
    """
    stones = 20
    player_turn = 1

    # Play until no stones remain
    while stones > 0:
        # Inform the players of how many stones are left to be taken
        print("There are " + str(stones) + " left.")

        # Depending on who's turn it is, ask them for their move,
        # make sure it's valid, then execute their move
        take = int(input("Player " + str(player_turn) + " would you like to remove 1 or 2 stones? "))
        if check_for_valid_entry(take):
            stones -= take
            if player_turn == 1:
                player_turn = 2
            else:
                player_turn = 1
        else:
            print("Please enter 1 or 2.")
        print()

    # When no stones remain, the player who's turn it is now
    # is the winner (since the last payer made a move and passed
    # the turn to the next player).
    print("Player " + str(player_turn) + " wins!")


def check_for_valid_entry(take):
    """
    Checks whether the Nimm move was valid, either a 1 or a 2
    :param take: Number of stones the user attempted to take
    :return: True if the move was valid, False otherwise.
    """
    if take == 1 or take == 2:
        return True
    return False


if __name__ == "__main__":
    main()
