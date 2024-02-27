from random_number import random_number
from random_alphabet import random_alphabet
from random_character import random_character
from random_emoji import random_emoji
from random_special_character import random_special_character

def main():
    print("Random Number:", random_number(1, 100))
    print("Random Alphabet:", random_alphabet())
    print("Random Character:", random_character())
    print("Random Special Character:", random_special_character())
    print("Random Emoji:", random_emoji())

if __name__ == "__main__":
    main()
