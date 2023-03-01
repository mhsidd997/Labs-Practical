# List Comprehension in Python
strings = ["HELLO PROGRAMMING", "WORLD", "BYE", "WOLRD"]
lowercased_strings = []
for word in strings:
    if(len(word) > 5):
        lowercased_strings.append(word.lower())

print(lowercased_strings)

print("x==========x==========x==========x\n")
#Pop the values from List
colors = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow', 'Teapink']
print("\n",colors)
colors.pop(0)
colors.pop(3)
colors.pop(4)
print("\n",colors)