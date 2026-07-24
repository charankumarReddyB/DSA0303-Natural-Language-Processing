from collections import Counter

text = "I love NLP I love Python NLP is interesting"

words = text.lower().split()

frequency = Counter(words)

print("Word Frequency:", frequency)
