from WordList import *
from keyboard import add_hotkey
from pyautogui import press, typewrite
from random import uniform


class Game:
    def __init__(self, lang: Lang, amount: int = 5):
        self.amount = amount
        self.words = WordList(lang, amount)
        self.out_words = []
        self.used_words = set()
        self.setup_kb()
        self.listen()


    def listen(self):
        while True:
            inp = input()
            self.out_words.clear()
            self.out_words = list(self.words.find_words(inp, self.used_words))

            print(f"|{"- "*10}-|")

            for index, word in enumerate(self.out_words):
                print(f"{index + 1} - {word}")

            print(f"|{"- "*10}-|\n")


    def setup_kb(self):
        for num in range(self.amount):
            add_hotkey(f"{(num+1)}"[-1], lambda num = num: self.kb_cmd(num)) # if num == 9 num +1 = 10 using [-1] 0 will be the hotkey


    def kb_cmd(self, num: int):
        try:
            press("backspace")
            word = list(self.out_words[num])
            for letter in word:
                typewrite(letter, uniform(0.001, 0.005))

            self.used_words.add("".join(self.out_words[num]))
            press("enter")

        except:
            pass
