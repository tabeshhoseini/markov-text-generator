import unicodedata
import random

successors = {}
window = []


def load_puncuations():
    puncs = {}
    try:
        with open("sample.txt", "r") as file:
            for line in file:
                for char in line:
                    category = unicodedata.category(char)
                    if category.startswith("P"):
                        puncs[char] = 1

            punctuation = "".join(puncs)
            return punctuation
    except FileNotFoundError:
        return ""


punctuation = load_puncuations()


def clean_word(word):
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


def process_words():
    try:
        for line in open("sample.txt", "r"):
            seq = line.replace("—", " ").split()
            for word in seq:
                cleaned = clean_word(word)
                create_triagram(cleaned)
    except FileNotFoundError:
        print("Error: 'sample.txt' not found. Cannot process words.")
        return False
    return True


def main():

    if not process_words():
        return

    if not successors:
        print("Error: No triagrams generated")
        return

    bigram = random.choice(list(successors))

    for i in range(20):
        last_word = bigram[1]
        possible_words = successors.get(bigram, [])

        if not possible_words:
            bigram = random.choice(list(successors))
            continue

        word = random.choice(possible_words)
        print(word, end=" ")

        bigram = (last_word, word)


if __name__ == "__main__":
    main()
