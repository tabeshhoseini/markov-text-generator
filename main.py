import unicodedata
import random

successors = {}
window = []
word = ""


def clean_word(word):
    puncs = {}
    for line in open("sample.txt", "r"):
        for char in line:
            category = unicodedata.category(char)
            if category.startswith("P"):
                puncs[char] = 1

    punctuation = "".join(puncs)

    return word.strip(punctuation).lower()


def add_to_successors(triagram):
    first, second, third = triagram

    if (first, second) not in successors:
        successors[(first, second)] = [third]
    else:
        successors[(first, second)].append(third)


def create_triagram(word):
    window.append(word)

    if len(window) == 3:
        add_to_successors(window)
        window.pop(0)


def proccess_words():
    for line in open("sample.txt", "r"):
        seq = line.replace("—", " ").split()
        for word in seq:
            clean_word(word)
            create_triagram(word)


proccess_words()

bigram = random.choice(list(successors))

for i in range(20):
    last_word = bigram[1]
    possible_words = successors[bigram]
    word = random.choice(possible_words)
    print(word, end=" ")

    bigram = (last_word, word)
