#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
words = str.split()
sentence = " ".join(words[5:7] + [words[-4]] + [words[0]])
print(sentence)
