#!/usr/bin/env python
import sys
import os
class ScoresDict():
    """
    This class objective is to decide which text within a sequence of texts is the most likely to be the 
    resultant of the ceaser decryption. 

    To do so, the algorithm will be trained to recognize trigrams (3 consecutive pairs of characters ) from 
    a given training data ( a book ). 

    Then, when a sequence of texts is given to the algorithm it will assign a score value to each text by 
    counting trigrams in the text. 

    The text that has higher score value is choosed as the most likely to be the original plaintext resultant
    from the decryption.

    """
    def __init__(self,training_file='the_hunger_games.txt'):
        self.training_text = open(training_file).read()
        self.counts = self.count_trigrams(self.training_text)

    def count_trigrams(self,text):
        """
        Creats a key-value dict of trigrams that contain the number of ocurrences for each seen trigram
        """
        counts = DefaultDict(1)
        for trigram in self.trigrams(text):
            counts[trigram] += 1

        return counts

    def trigrams(self,text):
        "Return a list of all consecutive trigrams of letters in text."
        return [text[i:i+3] for i in range(len(text) - 1)]

    def score(self, plaintext):
        "Returns a score for the given text based on how common english trigrams."
        return sum([self.counts[trigram] for trigram in self.trigrams(plaintext)])

    def argmax(self,sequence):
        "Return the element e of sequence with maximum score value."
        _, best_e = max([(self.score(e), e) for e in sequence])
        return best_e

class DefaultDict(dict):
    "Dictionary with a default value for unknown keys."
    def __init__(self, default):
        self.default = default

    def __getitem__(self, key):
        return self.get(key, self.default)
