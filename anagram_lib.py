''' anagram_lib contains classes and routines necessary 
to play Anagrams
'''

import random
import numpy as np

# Load Scrabble dictionary
scrabble_words = []

with open("twl06_scrabble_word_list.txt") as f:
	for line in f.readlines():
		scrabble_words.append(line[:-1].upper())

# Default Bananagrams board distribution
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

def letters_from_dist(dist):
	"""
	Given a distribution of letters in a dictionary format, eg. 
	{2: ["J", "K", "Q", "X", "Z"], 4: ["G"], etc.},
	where this example indicates that J, K, Q, X, Z should appear twice and G four times,
	letters_from_dist returns a randomized list of letters for the board. 
	"""
	letters = []
	
	for freq in dist:
		for letter in dist[freq]: 
			letters.extend([letter for i in range(freq)])

	return random.sample(letters, k = len(letters))

def letter_freqs(letters):
    """
    Given a word or list of letters, converts to 
    a numpy array of length 26 containing the frequency of each letter.
    """
    freqs = [0 for x in range(26)]
    for letter in letters:
        freqs[ord(letter)-ord("A")] = freqs[ord(letter)-ord("A")]+1
    
    return np.array(freqs)

def freqs_to_letters(freqs):
	"""
	Given letter frequences (eg. output of letter_freqs()),
	returns a list of letters
	"""
	letters = []
	n_letter = ord('A')
	for freq in freqs:
		letters.extend([chr(n_letter) for x in range(freq)])
		n_letter = n_letter + 1

	return letters

def is_word(word):
	""" 
	Checks the Scrabble dictionary to see whether a word exists.
	Restrict words to be at least 4 letters. 
	"""
	return (word in scrabble_words) & (len(word) >= 4)



class Board():

	def __init__(self, players, letters_dist = bananagrams_dist):
		"""
		Initialize board given player names 
		and distribution of letters (default is the Bananagrams distribution). 
		"""
		self.players = players # list of player names, from user input
		self.whos_turn = 0 # index of current player. It's currently player 0's turn. 
		words = {}
		for player in players:
			words[player] = []

		self.words = words # dictionary with players mapping to words owned by that player
		self.letters_down = letters_from_dist(letters_dist) # list of letters not yet visible
		self.letters_up = [] # list of visible, upturned letters

	def __str__(self):
		s = ""
		s+= "\n\n********* CURRENT BOARD *********"
		s+= "\n*** LETTERS: ***\n"
		for letter in self.letters_up:
			s += f"{letter}   "
		for x in range(len(self.letters_down)):
			s += "*   "

		s+= "\n*** WORDS: ***"
		for player in self.words:
			s+= f"\nPLAYER: {player}"
			for word in self.words[player]:
				s+= f"\n   {word}"
		return s

	def take_turn(self):
		"""
		Current player takes their turn by flipping over a letter. 
		Then update who the current player is.
		"""
		self.letters_up.append(self.letters_down.pop())

		# now it's the next player's turn
		self.whos_turn = (self.whos_turn + 1) % len(self.players)

	def word_from_letters(self, new_player, new_word):
		"""
		Player enters a new word from the upturned letters. Check to see if
		it is a valid new word, i.e. the following conditions hold:
		1. New word is in the Scrabble dictionary.
		2. New word is an anagram of some subset of the upturned letters. 
		"""

		# check that new word is in Scrabble dictionary
		check_0 = is_word(new_word)

		zeros = np.array([0 for x in range(26)]) # array of 26 zeros for comparison

		# check that new word is a subset of available letters 
		# (i.e. new word can only add available letters to old word)
		check_2 = np.all(letter_freqs(self.letters_up) - letter_freqs(new_word) >= zeros)

		if not (check_0 & check_2): 
			print(check_0)
			print(check_2)
			print("This is not a valid new word!")
			return

		# If it is a valid word, remove old word from old player and used letters from
		# upturned letters; add new word to new player. 
		self.letters_up = freqs_to_letters(letter_freqs(self.letters_up) - letter_freqs(new_word))
		self.words[new_player].append(new_word)

		# Flip over two new letters if a new word is successfully created
		# TO-DO: need to figure out how to end when letters run out
		self.letters_up.append(self.letters_down.pop())
		self.letters_up.append(self.letters_down.pop())


	def word_from_word(self, new_player, old_word, new_word): 
		"""
		Player enters a new word out of an old word. Check to see if 
		it is a valid new word, i.e. the following conditions hold:
		1. New word is in the Scrabble dictionary. 
		2. New word is an anagram of the old word + some subset of upturned letters,
		i.e. new word is longer than old word,
		includes the entirety of the old word, 
		and only adds available upturned letters to the old word. 
		"""

		# checking if old word exists and who the old word belongs to
		old_player = None
		for player in self.words:
			for word in self.words[player]:
				if word == old_word: 
					old_player = player

		if not old_player:
			print("The word you are trying to steal does not exist!")
			return


		zeros = np.array([0 for x in range(26)]) # array of 26 zeros for comparison

		# total set of available letters (old word letters AND upturned letters)
		available_letters = letter_freqs(old_word) + letter_freqs(self.letters_up)

		# check that new word is in Scrabble dictionary
		check_0 = is_word(new_word)

		# check that old word is a subset of new word (i.e. new word needs to use up entire old word)
		check_1 = np.all(letter_freqs(new_word)-letter_freqs(old_word) >= zeros)

		# check that new word is a subset of old word + available letters 
		# (i.e. new word can only add available letters to old word)
		check_2 = np.all(available_letters - letter_freqs(new_word) >= zeros)

		# check that new word is longer than old word
		check_3 = len(new_word) > len(old_word)

		if not (check_0 & check_1 & check_2 & check_3): 
			print("This is not a valid new word!")
			return

		# If it is a valid word, remove old word from old player and used letters from
		# upturned letters; add new word to new player. 

		self.words[old_player].remove(old_word)
		self.letters_up = freqs_to_letters(available_letters - letter_freqs(new_word))
		self.words[new_player].append(new_word)

		# Flip over two new letters if a new word is successfully created
		# TO-DO: need to figure out how to end when letters run out
		self.letters_up.append(self.letters_down.pop())
		self.letters_up.append(self.letters_down.pop())






