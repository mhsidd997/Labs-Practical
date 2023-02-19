# Identity Operators in Python
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

y = 7.2
if (type(y) is not int):
    print("true")
else:
    print("false")

# Membership Operator in Python
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]

for item in list1:
    if item in list2:
        print("overlapping")
    else:
        print("not overlapping")