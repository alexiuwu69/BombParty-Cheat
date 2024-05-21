from enum import Enum

class Lang(Enum):
    GERMAN = "german"


class WordList:
    def __init__(self, lang: Lang, amount: int = 5):
        self.amount = amount
        self.words = set(
            open(f"resources/wordlist-{lang}.txt") 
            .read() 
            .splitlines()
        )

    def find_words(self, splice: str) -> set:
        temp_words = []
        for word in self.words:
            if len(temp_words) == self.amount:
                break

            if splice in word:
                temp_words.append(word)

        return temp_words