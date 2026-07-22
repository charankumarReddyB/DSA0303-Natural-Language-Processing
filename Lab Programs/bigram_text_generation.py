import random

text = "I love natural language processing and I love machine learning"

words = text.split()

bigrams = {}

for i in range(len(words) - 1):
    word = words[i]
    next_word = words[i + 1]

    if word not in bigrams:
        bigrams[word] = []

    bigrams[word].append(next_word)

start = random.choice(words[:-1])
generated = [start]

for i in range(9):
    if start in bigrams:
        next_word = random.choice(bigrams[start])
        generated.append(next_word)
        start = next_word
    else:
        break

print("Generated Text:")
print(" ".join(generated))