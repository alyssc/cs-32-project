'''
Single-player version of Anagrams.
Anagrams is usually multi-player; this is to demonstrate usage of the Board class. 
'''

import sys
from anagram_lib import Board


def main():
    print("ANAGRAMS!")
    player = input("What's your name? ")

    # initialize board
    board = Board([player])

    # gameplay
    while len(board.letters_down) + len(board.letters_up) > 0:
        board.take_turn()

        print(board)

        new_word = input("Input an ANAGRAM if you can find one! Otherwise, press enter: ").upper()
        if new_word == "":
            continue

        old_word = input("If this is an ANAGRAM of the letters, press enter. Otherwise, enter the word you are changing: ").upper()
        if old_word == "":
            board.word_from_letters(player, new_word)
        else:
            board.word_from_word(player, old_word, new_word)



if __name__ == '__main__':
    main()
