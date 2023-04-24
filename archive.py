    
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



# checks if two words are anagrams
def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)
    
# comes up with anagram of letters
# def anagram(letters):


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