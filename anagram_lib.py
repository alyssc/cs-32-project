''' anagram_lib contains classes and routines necessary 
to play Anagrams
'''

# Load Scrabble dictionary
scrabble_words = []

with open("twl06_scrabble_word_list.txt") as f:
    for line in f.readlines():
        scrabble_words.append(line[:-1].lower())

# default Bananagrams board distribution
bananagrams_dist = {2: ["J", "K", "Q", "X", "Z"],
	3: ["B", "C", "F", "H", "M", "P", "V", "W", "Y"],
	4: ["G"],
	5: ["L"],
	6: ["D", "S", "U"],
	8: ["N"],
	9: ["T", "R"],
	11: ["O"],
	12: ["I"],
	13: ["A"],
	18: ["E"]}



class Player():
    """
    A Player object represents a player in the Anagrams game. 
    Each player has a name (user input), words currently held, a current score, 
    and total games played and won (implement the last two later). 
    """

    def __init__(self, name, words, score):
        self.name = name # name of player
        self.words = words # list of Word objects
        self.score = score # current score

        #self.games_played = games_played # total games played
        #self.games_won = games_won # total games played

    def __str__(self):
        return f'{self.name}'

    def print(self):
        print(self.__str__())


# class Word():
	"""
	A Word object represents a word in the Anagrams game. 
	Each word has 
	"""


# TO-DO: create a Word class with the following
# attributes: word, Player who owns the word currently, length

# TO-DO: create a Board class with the following
# attributes: players, words, letters_down, letters_up

class Board():

	def __init__(self, players, words, letters):
		self.players = players # list of player names, from user input
        self.words = words # dictionary with players mapping to words owned by that player
        self.letters_down = letters_down # list of letters not yet visible
        self.letters_up = letters_up # list of visible letters

    # allows insertion of letters based on a distribution
    # eg. {2: ['a','']}. 
    # default is normal Bananagrams letters distribution
    def insert_letters(dist = None):




# checks the Scrabble dictionary to see whether a word exists
def is_word(word):
    return word in scrabble_words
    
# checks if two words are anagrams
def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)
    
# Given a list of words (of players) and letters
# (on the board), determines whether 
# new_word is a valid new word or stolen word. 
# Words should be 4 or more letters.
# This function does not yet cover stealing words by adding more than one extra letter. 
def is_valid_steal(new_word, words, letters):
    if not is_word(new_word):
        print("Not a word!")
        return
    
    letters_as_str = "".join([str(i) for i in letters])
    if sorted(new_word) in sorted(letters_as_str):
        print(f"{new_word} is a valid steal from the communal letters!")
        words = words.append(new_word)
        # Need to also remove the used letters; figure out later
        return
    
    for word in words:
        for letter in letters:
            if is_anagram(new_word, word+letter):
                print(f"{new_word} is a valid steal from the letter '{letter}' and word '{word}'!")
                return
        
    
    print("Not a valid steal!")
    return None
    
# comes up with anagram of letters
# def anagram(letters):