from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer

porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")

words = ["running", "studies", "playing", "happiness"]

print("Word\tPorter\tLancaster\tSnowball")

for word in words:
    print(word, "\t",
          porter.stem(word), "\t",
          lancaster.stem(word), "\t\t",
          snowball.stem(word))