from enum import Enum

class Lang(Enum):
    GERMAN = "german.txt"
    GERMAN_POKEMON = "german-pokemon.txt"


class WordList:
    def __init__(self, lang: Lang, amount: int = 5):
        self.amount = amount
        self.words = set(
            open(f"resources/{lang}")
            .read() 
            .splitlines()
        )


    def find_words(self, splice: str, used_words) -> set:
        found_words = []
        for word in self.words:
            if len(found_words) == self.amount:
                break

            if splice in word and word not in used_words:
                found_words.append(word)

        return set(found_words) # removing potential dublicates