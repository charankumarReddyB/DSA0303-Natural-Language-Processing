from nltk.stem import PorterStemmer

ps = PorterStemmer()

word = input("Enter an English word: ")

stem = ps.stem(word)

print("Stemmed Word:", stem)