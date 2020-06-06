'''def sum(x,y):
    return x+y
def sub(x,y):
    return x-y   
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

a=sum(2,4)
print(a)
'''
def SI(principal=1000, time=3, rate=5):
    interest=principal*time*rate/100
    print("Interest Accumalated: ",interest)

SI(time=2,rate=10)