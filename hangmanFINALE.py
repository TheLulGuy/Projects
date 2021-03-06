import random

word_list = [
    'anger',
    'angry',
    'fish',
    'catfish',
    'mouse',
    'mice',
    'farming',
    'paper',
    'acacia',
    'bark',
    'cube',
    'glue',
    'tape',
    'scissors',
    'water',
    'pollution',
    'carpooling',
    'disease',
    'corona',
    'memes',
    'phone',
    'samsung',
    'nose',
    'noise',
    'gandhi',
    'bonus',
    'textbook',
    'notebook',
    'laptop',
    'smartphone',
    'phone',
    'lion',
    'cow',
    'dear',
    'bear',
    'bird',
    'eagle',
    'mountain',
    'alps',
    'himalayas',
    'mother',
    'father',
    'uncle',
    'autocomplete',
    'kite',
    'pewdiepie',
    'jacksepticeye',
    'markiplier',
    'nice',
    'tokyo',
    'anime',
    'ghoul'
    'doggo',
    'discombobulate',
    'testing']


def get_word():
    word = random.choice(word_list)
    return word.upper()


def play(word):
    # Creates a hifen version of the word
    word_completion = "-" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman")
    print(display_hangman(tries))
    print(word_completion)
    print("\n")
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)

            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)

            else:
                print("Good job,", guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)

                if "-" not in word_completion:
                    guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)

            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)

            else:
                guessed = True
                word_completion = word
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    
    if guessed:
        print("Congrats, you guessed the word. So you win ig")
    else:
        print("You ran out of tries. The word was " + word + ". Maybe next time.")


def display_hangman(tries):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]
def main():
    word = get_word()
    play(word)
    while True:
        answer = input("Play Again? (Y/N) ").upper() 
        if answer == "Y":
            word = get_word()
            play(word)
        elif answer == 'N':
            break
        else:
            print('Enter valid answer')


main()