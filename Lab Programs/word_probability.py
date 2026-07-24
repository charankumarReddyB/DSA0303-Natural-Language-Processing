from collections import Counter

text = "I love NLP I love Python"

words = text.lower().split()

frequency = Counter(words)
total = len(words)

word = input("Enter word: ")

probability = frequency[word] / total

print("Probability:", probability)
