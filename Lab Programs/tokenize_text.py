import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

text = input("Enter text: ")

tokens = word_tokenize(text)

print("Tokens:", tokens)
