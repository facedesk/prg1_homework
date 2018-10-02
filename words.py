sentence = input("write a sentence\n>")
words = sentence.split(" ")

print(type(sentence),type(words))
print(words)
words = sorted(words)
print(words)
sentence = " ".join(words)
print(sentence)

