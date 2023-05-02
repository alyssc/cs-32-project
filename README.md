# CS 32 Project: ANAGRAMS!

My project is an implementation of a version of Anagrams (https://en.wikipedia.org/wiki/Anagrams_(game)). The game instructions are as follows:

---

INSTRUCTIONS (adapted from Wikipedia): To begin, all letter tiles are face down on the board. Players then take turns flipping over tiles (i.e. pressing ENTER on the computer) until somebody notices a word of four or more letters. A player can form a word by: 
1. Using face-up letter tiles from the pool,
2. "Stealing" a word from another player by combining it with one or more tiles from the pool to make a new word (e.g., the word TRACK may be formed with a K from the pool and a player's CART),
3. OR combining one of their own words with additional tiles from the pool in the same way. 
When a player sees a word, they call it out loud immediately (irrespective of who flipped the last tile) and then enter in their ANAGRAM. Two tiles are flipped when a word is made or taken. The game then continues with further tiles being flipped. 

NOTE: Newly flipped tiles will always appear at the end of the visible letters; all other letters will be alphabetized. 

If two players call out words simultaneously, it's up to you to decide who called it first! 

All words must be at least four letters long. 

The game ends when all tiles are face up and no further words can be formed. Scores for each player is calculated with their words: a 3-letter word is worth 1 point, a 4-letter word 2 points, and so on. 

Enter an equal sign ("=") if you'd like to end the game early. Ties are allowed!

OPTIONAL HOUSE RULE: Only make anagrams which change the meaning of the word! Eg. do not add S to START in order to make STARTS. It's up to you to decide what counts! 

---

The implementation is played from one shell by running anagrams.py. 

anagram_lib.py contains the relevant routines and class (Board) to run anagram.py. The main data structure is the Anagrams Board, which contains the randomized letter tiles and a running record of which player has which words. The new_word method in Board allows for checking of new anagrams, which are either created from letter tiles or from existing words. 

This version of Anagrams uses the Bananagrams tile distribution and the Scrabble dictionary to check if words exist. These can be changed under anagram_lib.py to alternate distributions or dictionaries. 


