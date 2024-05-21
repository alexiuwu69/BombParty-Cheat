import requests
from bs4 import BeautifulSoup
from string import ascii_lowercase

allowed_letters = set(ascii_lowercase).union(set("äöü-0123456789ßé:"))


if __name__ == "__main__":
    url = "https://www.pokewiki.de/Pok%C3%A9mon-Liste"
    content = requests.get(url).text

    text = BeautifulSoup(content, "html.parser") \
        .get_text() \
        .split()

    with open("resources/german-pokemon.txt", "w", encoding="utf-8") as f:
        for i, line in enumerate(text):
            if line.strip().isnumeric():
                name = []
                for letter in text[i+1].lower():  # using lowercase so it's better
                    if letter in allowed_letters: # filtering for certain characters
                        name += letter
                
                f.write(f"{"".join(name)}\n")


# just run it, if there are new pokemon released 
# Only intended for german names, to compute english names, change the last line to: text[i+2]
# no guarantee that it works perfectly