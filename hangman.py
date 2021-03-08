import random
import string
import sys
# Write your code here


def create_hint(word, guess_set):
    hint = [letter if (letter in guess_set) and (letter in word) else '-' for letter in word]
    return ''.join(hint)


def check_guess(guess, hidden_word, hint):
    return (guess in hidden_word) and (guess not in hint)


def check_guess_word(hidden_word, hint):
    return hidden_word == hint


def get_guess():
    return input("Input a letter:").strip()


def check_not_lower_letter(guess):
    return not guess.islower()


def check_not_single_letter(guess):
    return len(guess) != 1


def check_not_english_letter(guess):
    return guess not in string.ascii_letters


def check_not_valid_guess(guess):
    is_not_valid = False
    if check_not_single_letter(guess):
        print("You should input a single letter")
        is_not_valid = True
    elif check_not_lower_letter(guess):
        print("Please enter a lowercase English letter")
        is_not_valid = True
    return is_not_valid


def game():
    while True:
        message = input('Type "play" to play the game, "exit" to quit:')
        if message == "play":
            break
        elif message == "exit":
            sys.exit()

    game_end = False
    tries = 8
    words = ['python', 'java', 'kotlin', 'javascript']
    guess_set = set()
    hidden_word = random.choice(words)
    print('H A N G M A N')
    while not game_end:
        hint = create_hint(hidden_word, guess_set)
        print()
        print(hint)
        guess = get_guess()
        if check_not_valid_guess(guess):
            continue
        if guess in guess_set:
            print("You've already guessed this letter")
            continue
        elif not check_guess(guess, hidden_word=hidden_word, hint=hint):
            print("That letter doesn't appear in the word")
            tries -= 1

        guess_set.add(guess)
        if check_guess_word(hidden_word, create_hint(hidden_word, guess_set)):
            print("You guessed the word!\nYou survived!")
            game_end = True
        elif tries == 0:
            print("You lost!")
            game_end = True


game()
