import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

ps = PorterStemmer()

text = input("Enter a paragraph: ")

words = word_tokenize(text)

print("Original Words:")
print(words)

print("\nStemmed Words:")
for word in words:
    print(ps.stem(word), end=" ")