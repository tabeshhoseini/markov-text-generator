import unicodedata

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
        words[word] = 1


print(words)
