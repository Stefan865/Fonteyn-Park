import string
import random

def pass_create(length, use_digits=True, use_letters=True, use_special_chars=True):
    characterList = ""

    if use_digits:
        characterList += string.digits
    if use_letters:
        characterList += string.ascii_letters
    if use_special_chars:
        characterList += string.punctuation

    password = [random.choice(characterList) for _ in range(length)]
    return "".join(password)
