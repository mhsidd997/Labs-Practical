string = input("Enter a string: ")
char = input("Enter a character: ")

starts_with = lambda string, char: string[0] == char

if starts_with(string, char):
    print("The string starts with the character ", char)
else:
    print("The string does not start with the character ", char)