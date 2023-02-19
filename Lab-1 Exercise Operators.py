# Identity Operators in Python
print("Identity Operators\n")
x = 6
if (type(x) is int):
    print("true")
else:
    print("false")

# if(type(y) y = 7.2    Written same as on the Lab File
# if (type(y) is not int):
#     print("true")
# else:
#     print("false")

# y = 7.2
# if (type(y) is not int):
#     print("true")
# else:
#     print("false")

print("x==========x==========x==========x\n")
# Membership Operator in Python
print("Membership Operator\n")
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]

for item in list1:
    if item in list2:
        print("overlapping")
    else:
        print("not overlapping")

print("x==========x==========x==========x\n")
# Floor Division and Exponent and Assign
print("Floor Division and Exponent and Assign\n")
a = 8
res = a//3
res2 = a**5
print("floor divide=",res)
print("exponent=",res2)

# a//=3     Written same as on the Lab File
# a**=5
# print("floor divide=",a)
# print("exponent=",a)

print("x==========x==========x==========x\n")
# Bitwise Operators
print("Bitwise Operators\n")
a=60
b=12
c=0

c = a&b
print("Line 1",c)
c = a|b
print("Line 2",c)
c = a^b
print("Line 3",c)
c = ~a
print("Line 4",c)
c = a<<2
print("Line 5",c)
c = a>>2
print("Line 6",c)