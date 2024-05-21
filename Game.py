from WordList import *
from pyperclip import copy

class Game:
    def __init__(self, lang: Lang, amount: int = 5):
        self.words = WordList(Lang.GERMAN.value, amount)
        self.listen()

    def listen(self):
        while True:
            inp = input()
            out_words = self.words.find_words(inp)
            copy(out_words[0])
            print(f"|{"- "*10}-|")

            for word in out_words:
                print(word)

            print(f"|{"- "*10}-|")
            print()