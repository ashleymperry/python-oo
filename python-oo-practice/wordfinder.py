import random

class WordFinder:
    """Machine for finding random words from dictionary.
    
    >>> Wordfinder.random() in ["cat", "dog", "porcupine"]
    True

    >>> WordFinder.random() in ["carrot", "red", "hey"]
    True

    >>> WordFinder.random() in ["sand", "child", "lawn"]
    True
    """
words = []
with open('/usr/share/dict/words') as WordFinder:
    for line in WordFinder:
        words.append(line.strip())
    random.choice(words)
    
