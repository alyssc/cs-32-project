''' anagram_lib contains classes and routines necessary 
to play Anagrams
'''

import random
import numpy as np

#### Load relevant data ####

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


#### Helper functions for Board class ####
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
	if word not in scrabble_words:
		print("That's not in our dictionary!")
		return False
	if len(word) < 4:
		print("That's too short! Words must be 4 or more letters.")
		return False

	return True



class Board():

	def __init__(self, players, letters_dist = bananagrams_dist):
		"""
		Initialize Anagrams board given player names 
		and a distribution of letters (default is the Bananagrams distribution). 
		"""
		self.players = players # list of player names, from user input
		self.whos_turn = 0 # index of current player. It's currently player 0's turn. 
		words = {}
		for player in players:
			words[player] = []

		self.words = words # dictionary with players mapping to words owned by that player
		self.letters_down = letters_from_dist(letters_dist) # list of letters not yet visible
		self.letters_up = [] # list of visible, upturned letters
		self.end_game = False # indicator to begin endgame when letters run out

		# Starts game with 4 tiles flipped upwards! Can omit this
		self.flip_letter(3) # 3 flips due to how anagrams.py is ordered

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
		s+= "\n"
		return s

	def flip_letter(self, n = 1):
		"""
		Turns over n letters if there are letters left. 
		If there are <n letters left, turn over the remaining letters
		and begin last turn. 
		"""

		for i in range(n):
			try:
				self.letters_up.append(self.letters_down.pop())
			except:
				self.end_game = True # this doesn't immediately end the game but rather triggers a game ending the next turn

	def take_turn(self):
		"""
		Current player takes their turn by flipping over a letter. 
		Then update who the current player is.
		"""
		self.flip_letter()

		# now it's the next player's turn
		self.whos_turn = (self.whos_turn + 1) % len(self.players)

	def score(self):
		"""
		Calculates scores and prints out winner. 
		Score for each player is calculated by adding the (length-3) of each word
		in order to incentivize longer words. 
		"""
		scores = []

		for player in self.players:
			score = 0
			for word in self.words[player]:
				score += len(word)-2
			
			scores.append(score)

		# Allows for multiple winners
		winners = np.argwhere(scores == np.max(scores)).flatten()

		print("\n")

		for w in winners:
			print(f"{self.players[w]} WON! ")

		print("\n**ALL SCORES**")

		for i in range(len(self.players)):
			print(f"{self.players[i]}: {scores[i]}")

		print("Game ended.")

	def new_word(self, new_player, new_word):
		"""
		Player enters a new word. Check to see if
		it is a valid new word, i.e. the following conditions hold:

		OPTION A: the new word is created only from the center letters
		1. New word is in the Scrabble dictionary.
		2. New word is an anagram of some subset of the upturned letters. 

		OR

		OPTION B: the new word is created from the center letters and an old word
		1. New word is in the Scrabble dictionary. 
		2. New word is an anagram of the old word + some subset of upturned letters,
		i.e. new word is longer than old word,
		includes the entirety of the old word, 
		and only adds available upturned letters to the old word. 

		A new word can be created multiple ways. new_word() prioritizes 1) making words
		from the letter tiles, 2) stealing words, and 3) making words from the player's own words. 
		Note that there is no disambiguation among different steals or word makings. 
		"""

		# check that new word is in Scrabble dictionary
		if not is_word(new_word): 
			print("Not a valid new word. Try again!")
			return False

		zeros = np.array([0 for x in range(26)]) # array of 26 zeros for comparison

		# OPTION A: check if new word can be made of the upturned letter tiles
		check_1 = np.all(letter_freqs(self.letters_up) - letter_freqs(new_word) >= zeros)

		if check_1: 
			# If it is a valid word from the upturned tiles, 
			# remove old word from old player and used letters from
			# upturned letters; add new word to new player. 
			self.letters_up = freqs_to_letters(letter_freqs(self.letters_up) - letter_freqs(new_word))
			self.words[new_player].append(new_word)

			# Flip over two new letters if a new word is successfully created
			self.flip_letter(2)

			print(f"{new_player} has created the word {new_word}!")
			return True


		# OPTION B: checking if old word exists and who the old word belongs to
		old_player = None
		old_word = None
		to_break = False

		for player in self.words:
			for word in self.words[player]:

				# check to see if the new word can be made out of this word
				available_letters = letter_freqs(word) + letter_freqs(self.letters_up)

				# check that old word is a subset of new word (i.e. new word needs to use up entire old word)
				check_1 = np.all(letter_freqs(new_word)-letter_freqs(word) >= zeros)

				# check that new word is a subset of old word + available letters 
				# (i.e. new word can only add available letters to old word)
				check_2 = np.all(available_letters - letter_freqs(new_word) >= zeros)

				# check that new word is longer than old word
				check_3 = len(new_word) > len(word)

				# found a valid old word! 
				if check_1 & check_2 & check_3: 

					# this if statement handles case where multiple instances of old_word
					# to make sure that other player's words are stolen before own word
					if old_player:
						if old_player == new_player:
							old_player = player
							old_word = word
					else:
						old_player = player
						old_word = word


		if not old_player:
			print("Not a valid steal!")
			return False


		# If it is a valid word, remove old word from old player and used letters from
		# upturned letters; add new word to new player. 

		self.words[old_player].remove(old_word)
		self.letters_up = freqs_to_letters(available_letters - letter_freqs(new_word))
		self.words[new_player].append(new_word)

		# Flip over two new letters if a new word is successfully created
		self.flip_letter(2)

		if new_player == old_player:
			print(f"{new_player} has created the word {new_word} out of {old_word}!")
		else:
			print(f"{new_player} has stolen {old_word} from {old_player} to create {new_word}!")
		return True











