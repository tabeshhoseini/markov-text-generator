import unicodedata
import random

successors = {}
window = []
word = "hear"


def clean_word(word):
    puncs = {}
    for line in open("sample.txt", "r"):
        for char in line:
            category = unicodedata.category(char)
            if category.startswith("P"):
                puncs[char] = 1

    punctuation = "".join(puncs)

    return word.strip(punctuation).lower()


def add_to_successors(bigram):
    first, second = bigram

    if first not in successors:
        successors[first] = [second]
    else:
        successors[first].append(second)


def create_bigram(word):
    window.append(word)

    if len(window) == 2:
        add_to_successors(window)
        window.pop(0)


def proccess_words():
    for line in open("sample.txt", "r"):
        seq = line.replace("—", " ").split()
        for word in seq:
            clean_word(word)
            create_bigram(word)


proccess_words()

for i in range(10):
    possible_words = successors[word]
    word = random.choice(possible_words)
    print(word, end=" ")
