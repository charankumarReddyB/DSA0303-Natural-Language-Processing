from collections import Counter
from nltk.util import bigrams

text = "I love NLP I love Python I love AI"

words = text.lower().split()

unigram_freq = Counter(words)
bigram_freq = Counter(bigrams(words))

print("Unigram Frequency:")
print(unigram_freq)

print("\nBigram Frequency:")
print(bigram_freq)
