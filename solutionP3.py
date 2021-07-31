#This is my solution for problem 3. You may as well see my notes in the PDF file.
import random
all_words = []
with open(r'words.txt', 'r') as f:      #declare the local path for the opening of the file. I put it in the same
    for line in f:                      #folder with the .py file.
        for word in line.split():
            all_words.append(word)


def get_word():
    word = random.choice(all_words)
    return word.lower()


def play(word):
    word_to_complete = "_" * len(word)
    guessed_letters = []
    num_of_guessed_letters = 0
    correct_guesses = 0
    guessed = False
    number_of_tries = 5
    print("I am thinking of a word that is", len(word), "letters long! Try to guess this word!")
    print("you have", number_of_tries, "guesses left!")

    while not guessed and number_of_tries > 0:
        guess = input("Please enter a letter: ")
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print("wrong guess!")
                number_of_tries -= 1
                guessed_letters.append(guess)
            else:
                print("good guess!")
                guessed_letters.append(guess)
                number_of_tries -= 1
                correct_guesses += 1
                word_as_list = list(word_to_complete)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                    num_of_guessed_letters += 1
                word_to_complete = "".join(word_as_list)
                if "_" not in word_to_complete:
                    guessed = True
        else:
            print("Not a valid guess. Please enter a letter of the English alphabet.")
        print(word_to_complete)
        if not guessed and number_of_tries >=1:
            print("you have", number_of_tries, "guesses left!")

    guess_word = input("Please enter the corresponding word: ").lower()
    if guess_word == word:
        guessed = True
    else:
        guessed = False
    if guessed:
        score = 100 + (num_of_guessed_letters * correct_guesses)
        print("You win! Your score is:", score)
    else:
        score = num_of_guessed_letters * correct_guesses
        print("You lost. The word was " + word + ". Your score is:", score)
def main():
    word = get_word()
    play(word)


if __name__ == "__main__":
    main()