import random
import string

def random_special_character():
    special_chars = string.punctuation
    return random.choice(special_chars)
