def SetList(values):
    list = []
    for i in values:
        list.append(i)
    print(list)
 
SetList(['Canada','USA','Mexico','Australia'])

print("x==========x==========x==========x\n")
#Counts from 0 to 100
for i in range(1,101,1):
    print(i, end = " ")

print("\nx==========x==========x==========x\n")
#Multiplication Table of 5
for i in range(1,11,1):
    print("%d x %d = %d"%(5,i,5*i))

print("x==========x==========x==========x\n")
#Backward Count from 10 to 1
for i in range(10,0,-1):
    print(i, end = " ")

print("\nx==========x==========x==========x\n")
#Count even to 10
for i in range(0,11,2):
    print(i, end = " ")

print("\nx==========x==========x==========x\n")
#Sum from 100 to 200
sum = 0
for i in range(100,200,1):
    sum += i
print("Sum is ",sum)