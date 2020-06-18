apple=10
mango=20

def fruits():
    apple=15
    print("No of apple:",apple)
fruits()
print(apple)

def mango():
    global mango
    mango=30
    print("no of Mango :",mango)
mango()

print(mango)