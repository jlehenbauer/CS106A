
def main():
    """
    Hosts a game of Nimm to be played by two players.
    """
    one_player_mode = False
    stones = 20
    player_turn = 1

    # Ask the user if they wish to play one-player mode.
    choice = input("Would you like to play against me, the computer? (y for yes) ")
    if choice.lower() == 'y':
        one_player_mode = True
        print("You go first!")

    # Play until no stones remain
    while stones > 0:
        # Inform the players of how many stones are left to be taken
        print("There are " + str(stones) + " left.")

        # If the computer player is enabled and it's currently
        # the computer's turn, make their move.
        if one_player_mode and player_turn == 2:
            take = take_computer_player_turn(stones)

        # If it's a 2 player game or player 1's turn,
        # ask them for their move.
        else:
            take = int(input("Player " + str(player_turn) + " would you like to remove 1 or 2 stones? "))

        # Check that the last move was valid
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


def take_computer_player_turn(stones):
    """
    Computer player AI to decide how many stones to remove.
    Will always win :)
    :param stones: Number of stones remaining at start of turn
    :return: Number of stones to take
    """
    # Ending cases: if stones < 4, choose
    # 1 or 2 appropriately to leave player 1
    # with 1 stone.
    if stones == 3:
        print("I'm removing 2 stones.")
        return 2
    elif stones == 2:
        print("I'm removing 1 stone.")
        return 1

    # Until we reach the ending cases, remove
    # stones to keep the remaining number even,
    # so player 1 is forced to choose at 4 stones
    # remaining.
    elif stones % 2 == 0:
        print("I'm removing 2 stones.")
        return 2
    else:
        print("I'm removing 1 stone.")
        return 1


if __name__ == "__main__":
    main()
