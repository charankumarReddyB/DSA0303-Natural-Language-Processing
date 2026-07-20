from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["universal", "university", "running", "better", "children"]

print("Word\tStem")

for word in words:
    print(word, "\t", ps.stem(word))

print("\nExamples:")
print("Overstemming : universal -> univers")
print("Understemming: better -> better")