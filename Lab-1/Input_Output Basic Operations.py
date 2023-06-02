#Swapping 4 Variables Program
print("Please enter 4 Numbers for Swapping:")
a = input()
b = input()
c = input()
d = input()
print(f"Numbers before swapping: a={a}, b={b}, c={c}, d={d}\n")
t1 = a;a = d;d = t1
t2 = b;b = c;c = t2
print(f"Numbers before swapping: a={a}, b={b}, c={c}, d={d}\n")

print("x==========x==========x==========x\n")
#Calculate Temprature Celsius to Fahrenheit
print("Please enter Celsius Temperature:")
tempC = float(input())
tempF = 9.0*(tempC/5.0)+32.0
print(f"Celsius Temperature: {tempC}*C")
print("Fahrenhrit Temperature: %.2f\n"%tempF)