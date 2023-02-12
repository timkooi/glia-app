import random
from .models import Word

def jumble_word(word: Word):
    string = word.word
    if len(string) <= 1:
        return {"jumbled_word": string}
    jumbled = ''.join(random.sample(string, len(string)))
    if jumbled == string:
        jumbled = jumble_word(word)
    return {"jumbled_word": jumbled}

