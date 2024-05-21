import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = "https://www.pokewiki.de/Pok%C3%A9mon-Liste"
    content = requests.get(url).text

    text = BeautifulSoup(content, "html.parser") \
        .get_text() \
        .split()

    with open("resources/german-pokemon.txt", "w", encoding="utf-8") as f:
        for i, line in enumerate(text):
            if line.strip().isnumeric():
                f.write(f"{text[i+1]}\n")


    # just run it, if there are new pokemon released 
    # Only intended for german names, to compute english names, change the last line to: f.write(f"{text[i+2]}\n)
    # no guarantee that it works perfectly