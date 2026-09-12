# sentence = "The red dog ate cake"

# keywords = input("enter two words: ").split(" ")

# index1 = sentence.index(keywords[0])
# index2 = sentence.index(keywords[1])

# if index1 == -1 or index2 == -1:
#     raise Exception("not matched keywords")
    

# minIdx = 0
# minWord = ""
# if index1 <= index2:
#     minIdx = index1
#     minWord = keywords[0]
# else:
#     minIdx = index2
#     minWord = keywords[1]

# maxIdx = 0
# maxWord = ""
# if index1 > index2:
#     maxIdx = index1
#     maxWord = keywords[0]
# else:
#     maxIdx = index2
#     maxWord = keywords[1]


# res = sentence[minIdx+len(minWord):maxIdx]
# print("minIdx: " + str(minIdx) + ", maxIdx: " + str(maxIdx))
# print(res.strip())

firstWord = input("Type the word on the left\n").lower()
secondWord = input("Type the word on the right\n").lower()
sentence = "The red dog and the blue dog ate cake with the green dog"
sentenceSplit = sentence.split(" ")
words = sentence.lower().split(" ")
wordLocations = dict(enumerate(words))
wordIndexes = {}

for index, word in wordLocations.items():
    if word in wordIndexes.keys():
        wordIndexes[word] += [index]
    else:
        wordIndexes[word] = [index]

for index in wordIndexes[firstWord]:
    if index + 2 in wordIndexes[secondWord]:
        print(sentenceSplit[index:index + 3])