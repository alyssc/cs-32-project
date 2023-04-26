'''
Non-networked version of Anagrams.
This version allows for multiple players, acting as a helper tool for players. 
'''

import sys
from anagram_lib import Board


def main():
    print("Welcome to ANAGRAMS!")

    instructions = """INSTRUCTIONS (adapted from Wikipedia): To begin, all letter tiles are face down on the board. Players then take turns flipping over tiles (i.e. pressing ENTER on the computer) until somebody notices a word of four or more letters. A player can form a word by: 
\n1. Using face-up letter tiles from the pool,
\n2. "Stealing" a word from another player by combining it with one or more tiles from the pool to make a new word (e.g., the word TRACK may be formed with a K from the pool and a player's CART),
\n3. OR combining one of their own words with additional tiles from the pool in the same way. 
\nWhen a player sees a word, they call it immediately (irrespective of who flipped the last tile) and then enter in their ANAGRAM. Two tiles are flipped when a word is made or taken. The game then continues with further tiles being flipped.
\nAll words must be at least three letters long. 
\nThe game ends when all tiles are face up and no further words can be formed. Scores for each player is calculated with their words: a 3-letter word is worth 1 point, a 4-letter word 2 points, and so on. 
\nEnter an equal sign ("=") if you'd like to end the game early. Ties are allowed!
"""
    print(instructions)

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

