'''
How many times does a letter appear in a string?

How many times does a word appear in a sentence?
'''
sentence = input("enter a word")

words = sentence.split(" ")

wordCount = {} # dictionary

for word in words:
    if(word in wordCount):
        wordCount[word] += 1
    else:
        wordCount[word] = 1
print(wordCount)
