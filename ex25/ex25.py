def break_words(stuff):
    """This function will break up words for us."""
    word = stuff.split(' ')
    return word

def sort_words(words):
    """Sort the words"""
    return sorted(words)

def print_first_word(words):
    """Print the first word afetr popping it off"""
    word = words.pop(0)
    print(word)

def print_last_word(words):
    """Print the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Take in a full sentence and return the sorted."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last(sentence):
    """Print the first and the last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(sentence):
    """Sort the words then print the first and the last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)