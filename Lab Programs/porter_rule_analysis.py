from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["running", "studies", "playing", "happiness", "relational"]

print("Original\tStemmed")

for word in words:
    print(word, "\t", ps.stem(word))