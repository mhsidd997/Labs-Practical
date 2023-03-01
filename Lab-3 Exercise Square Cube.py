numbers = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, numbers))
cubed = list(map(lambda x: x**3, numbers))

print("Original List:", numbers)
print("Squared List:", squared)
print("Cubed List:", cubed)