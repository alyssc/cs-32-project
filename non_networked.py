'''
Non-networked version of Anagrams.
This version allows for multiple players, acting as a helper tool for players. 
'''

import sys
from anagram_lib import Board


def main():
    print("ANAGRAMS!")

    while True: 
        players = input("Enter player names separated by spaces: ")
        if not len(players) == 0:
            break
        print("Please enter at least one player name. ")

    # initialize board
    players = players.split()
    board = Board(players)

    # gameplay
    while len(board.letters_down) + len(board.letters_up) > 0 and not board.end_game:

        board.take_turn()
        print(board)

        while True: 
            new_word = input("Input an ANAGRAM if you can find one! Otherwise, press enter: ").upper()
            if new_word == "":
                break

            # code to end game
            if new_word == "=":
                board.end_game = True
                break

            while True:
                new_player = input("Enter name of player who is making this word: ")
                if new_player in players: break
                print("This player name doesn't exist! Try again. ")

            if board.new_word(new_player, new_word):
                print(board)

    board.score()




if __name__ == '__main__':
    main()

