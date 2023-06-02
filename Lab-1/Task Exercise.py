#Exercise

list=[]

def PrintNumbers(x):
    for numb in range(0,x,1):
        print(numb)
        list.append(numb)


x = int(input("Please enter number to print series from 0: "))
PrintNumbers(x)
print("\nPrinting the count of 2 in list and list:")
print("List Count: ",list.count(2))
print(list)