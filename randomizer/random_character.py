import random
import string

def random_character():
    all_chars = string.ascii_letters + string.digits + string.punctuation
    return random.choice(all_chars)
