from itertools import product

word = ["к", "а", "л", "и", "й"]

wordlist = list(product(word, repeat=6))
string = ["".join(words) for words in wordlist]

string = list(filter(lambda x: x[0] != 'й' and x[5] != "й", string))

print(len(string))
