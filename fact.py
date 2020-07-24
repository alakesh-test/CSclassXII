#q: Write a function to find the factorial of a natural number.
# 5 --> 5x4x3x2x1 or 5 --> 1x2X3X4X5

def Fact(n):
    f=1
    for i in range(1,n+1):        # range(5) --> 0 1 2 3 4
           f=f*i
    return f

#__main

x= int(input("Enter a value to calculte factorial :"))
val=Fact(x)
print("The factorial of ",x, "is : ",val)
print("Hello World")
