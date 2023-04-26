'''
Non-networked version of Anagrams.
This version allows for multiple players, acting as a helper tool for players. 
'''

import sys
from anagram_lib import Board


def main():
    print("ANAGRAMS!")
    players = input("Enter player names separated by spaces: ")

    # initialize board
    board = Board(players.split())

    # gameplay
    while len(board.letters_down) + len(board.letters_up) > 0:
        board.take_turn()

        print(board)

        new_word = input("Input an ANAGRAM if you can find one! Otherwise, press enter: ").upper()
        if new_word == "":
            continue

        old_word = input("If this is an ANAGRAM of the letters, press enter. Otherwise, enter the word you are changing: ").upper()
        
        while True:
            new_player = input("Enter name of player who is making this word: ")
            if new_player in players: break
            print("This player name doesn't exist! Try again. ")

        if old_word == "":
            board.word_from_letters(new_player, new_word)
        else:
            board.word_from_word(new_player, old_word, new_word)



if __name__ == '__main__':
    main()

