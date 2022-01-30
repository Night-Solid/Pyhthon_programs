from words import words
import random
import string
from visual import lives_visual_dict


def get_valid_word(words):
    word = random.choice(words)
    while " " in word or "-" in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_valid_word(words).upper()
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used = set()
    live = 10
    while len(word_letter) > 0 and live > 0:
        # gitting the input
        # letters used by the player.
        word_list = [letter if letter in used else "-" for letter in word]
        print("the right letters guessed are: ", " ".join(word_list))
        print(
            "you have ",
            live,
            " left!! \nthese letters has been used by u: \
                ",
            " ".join(used),
        )
        print(lives_visual_dict[live])
        guess = input("enter a letter: ").upper()
        if guess in alphabet - used:
            used.add(guess)
            if guess in word_letter:
                word_letter.remove(guess)
            else:
                live -= 1
                print("Come on you lost a live!")
        elif guess in used:
            print(f"the letter - {guess} already guessed.")
        else:
            print("not a valid character.")
    if live == 0:
        print(lives_visual_dict[0])
        print("YOU DIED, sorry. The word was", word)
    else:
        print("the word is:", word)
        print("YOU WON!!")


hangman()
