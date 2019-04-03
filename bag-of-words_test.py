from nltk.tokenize import word_tokenize
from collections import Counter

# process this text to anlyse
text = """The cat is in the box. The cat likes the box. The box is over the cat."""

# show us the bag of words by tokenising the 'text'
print(Counter(word_tokenize(text)))


#tokenise words and print the most 3 common words of these letters
print("Three most common words are :", Counter(word_tokenize(text)).most_common(3))