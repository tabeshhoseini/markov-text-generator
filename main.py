import unicodedata
import random

words = {}
window = []
bigrams = {}


def clean_word(word):
    puncs = {}
    for line in open("sample.txt", "r"):
        for char in line:
            category = unicodedata.category(char)
            if category.startswith("P"):
                puncs[char] = 1

    punctuation = "".join(puncs)

    return word.strip(punctuation).lower()


def proccess_words():
    for line in open("sample.txt", "r"):
        seq = line.replace("—", " ").split()
        for word in seq:
            clean_word(word)
            create_bigram(word)


def create_bigram(word):
    window.append(word)

    if len(window) == 2:
        bigram = tuple(window)
        if bigram not in bigrams:
            bigrams[bigram] = 1
        else:
            bigrams[bigram] += 1

        window.pop(0)


# word_list = list(words)
# weights = words.values()

# print(random.choices(word_list, weights=weights, k=5))

proccess_words()
print(bigrams)
