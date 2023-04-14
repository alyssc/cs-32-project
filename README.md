# CS 32 Project: Lofi Maker

(no project partners)

My project (new idea) involves implementing a version of Anagrams (https://en.wikipedia.org/wiki/Anagrams_(game)). Roughly, the game is as follows: "The game pieces are a set of tiles with letters on one side. Tiles are shuffled face-down then turned over one by one, players forming words by combining them with existing words, their own or others'" (from the Wikipedia article). 

So far, I've created various helper functions which I think will be useful. The main helper function is is_valid_steal, which, given a board (i.e. collection of words and letters), determines whether a given new word is a valid steal (or newly created word, if chosen from the board). I have also imported a word dictionary which will be the main non-user input/data involved. 

My vision involves a multi-player game (I will start with just two players though) with one server and multiple clients. I plan on creating classes for the relevant objects in the game, for example for Players and Words. I will also have a simple user interface on the console for each client which involves printing the board at every turn; the board includes currently visible letters "in the middle" and each player's words. I have yet to figure out the timing so that the player who finds a word first gets to steal it. 

Note: I plan on using .py scripts but am using Jupyter Notebook to develop and test functions right now. 