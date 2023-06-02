pcount=0
ncount=0
count=int(input("how many numbers you want?"))
i=1
while(i<=count):
    num=int(input("enter number "))
    if(num>=0):
        pcount += 1
    else:
        ncount += 1
    i += 1
print("Positive",pcount)
print("Negative",ncount)