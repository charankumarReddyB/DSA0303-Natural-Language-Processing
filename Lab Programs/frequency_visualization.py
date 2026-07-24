from collections import Counter
import matplotlib.pyplot as plt

text = "I love NLP I love Python I love AI"

words = text.lower().split()

frequency = Counter(words)

plt.bar(frequency.keys(), frequency.values())

plt.xlabel("Words")
plt.ylabel("Frequency")
plt.title("Word Frequency Distribution")

plt.show()
