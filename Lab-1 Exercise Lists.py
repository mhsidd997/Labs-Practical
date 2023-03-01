print(dir(list))

print("\nHelp Lists:",help(list.reverse))

print("x==========x==========x==========x\n")
stringWords = []
n = 4;count = 0
print("Please enter 4 words:")
for i in range(0,n):
    wordList = input()
    stringWords.append(wordList)
print("String Words: ", stringWords)
for word in stringWords:
    if len(word) >= 2 and word[0] == word[- 1]:
        count+=1
print("Result: ",count)