def arithmetic(x,y):    
    '''Function that returns Multiple Values'''
    return x+y, x-y, x*y, x/y, x**y
    print("Thank you for using")
#__main_
val=arithmetic(6,2)
print(val)
print(type(val))
add,sub,multi,div,power=arithmetic(3,2)
print("Arithmeti Operation",add,sub,multi,div,power)