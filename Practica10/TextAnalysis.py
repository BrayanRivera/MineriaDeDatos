from wordcloud import WordCloud
from collections import Counter
import matplotlib.pyplot as plt


def open_file(path: str) -> str:
    content = ""
    with open(path, "r") as f:
        content = f.readlines()
    return " ".join(content)

all_words = ""
frase = open_file("Practica10/dataset.txt") 
palabras = frase.rstrip().split(" ")

Counter(" ".join(palabras).split()).most_common(10)
for arg in palabras:
    tokens = arg.split()
    all_words += " ".join(tokens) + " "

print(all_words)
wordcloud = WordCloud(
    background_color="white", min_font_size=5
).generate(all_words)

plt.close()
plt.figure(figsize=(10, 10), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig("img/word_cloud.png")
plt.close()