import unicodedata
import random

words = {}


def clean_word(word):
    puncs = {}
    for line in open("sample.txt", "r"):
        for char in line:
            category = unicodedata.category(char)
            if category.startswith("P"):
                puncs[char] = 1

    punctuation = "".join(puncs)

    return word.strip(punctuation).lower()


for line in open("sample.txt", "r"):
    seq = line.replace("—", " ").split()
    for word in seq:
        clean_word(word)
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1

word_list = list(words)
weights = words.values()

print(random.choices(word_list, weights=weights, k=5))
