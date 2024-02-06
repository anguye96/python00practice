import random

class WordFinder:
    "finding random words from dictionary"

    def __init__(self,path):
        dict_file = open(path)
        self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")
    def parse(self,dict_file):
        return [w.strip() for w in dict_file]

    def random(self):
        return random.choice(self.words)

class SpecialWordsFinder(WordFinder):
    def parse(self,dict_file):
        return[w.strip() for w in dict_file]
            if w.strip() and not w.startswith("#")