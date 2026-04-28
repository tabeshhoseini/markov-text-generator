words = []

with open("sample.txt", "r") as file:
    words = file.read().split()

print(words)
