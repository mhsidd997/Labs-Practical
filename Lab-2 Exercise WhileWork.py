def SetList(values):
    list = []
    count = 0
    while(len(values) >= count):
        list.append(values.pop(count))
        count+=1
    print(list)
 
SetList(['Canada','USA','Mexico'])

print("x==========x==========x==========x\n")
#Sum from 100 to 200
sum = 0
startRange = 100
endRange = 200
while(startRange < endRange):
    for i in range(0,2):
        print(i, end = " ")
    sum += startRange
    startRange+=1
print("\nSum is ",sum)