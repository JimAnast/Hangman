# Hangman
Implementation of the word game "Hangman"


We implement a small game called "Hangman" where the computer selects a random word from a list of words and the player tries to guess the selected word. Here are the different steps for this game:

The computer will select a random word from a list of words (words.txt) and let the player know how many letters in the selected word
At the beginning, the user is given 5 chances to guess the letters of the selected word
For each guess, the computer should tell the player if the letter is in the selected word and print the position of these letter in the word (example: --a--a-, with "-" is an unknown letter)
After 5 guesses, the player should enter the entire word: if it is correct they will get a score of 100+ (number of guessed letters * correct guesses), otherwise, they will get a score of (number of guessed letters * correct guesses).

Example:

I am thinking of a word that is 8  letters long! Try to guess this word!

you have  5 guesses left!

Please enter a letter: a

wrong guess!

--------

you have  4 guesses left!
Please enter a letter: e

good guess!

e----e-e

you have  3 guesses left!
Please enter a letter: d

good guess!

e-d--e-e

you have  2 guesses left!
Please enter a letter: t

wrong guess!

e-d--e-e

you have  1 guesses left!
Please enter a letter: p

good guess!
e-dp-e-e

Please enter the corresponding word: endpiece

You win! Your score is :  115



I used lists for the making of that game. 
The player has 5 guesses of letters and 1 guess of the word. The game will stop the letter guesses if the player finds all of the letters in less than 5 guesses and it will continue by asking the player to write the entire word correctly. 
Even if the player has found the word through the letter guesses, they will need to type correctly the whole word in order to win and get the 100 bonus. For example, if the word has been revealed from just 3 letter guesses, the game will skip the remaining (2) letter guesses and it will ask from the player to type the word. 
