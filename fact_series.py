def fact(n):
    '''
    This function finds factorial
    '''
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def series(x,n):
    '''
    This function to calculate a particular series value'''
    sum=1
    for i in range(1,n+1):
        sum = sum+(x**i)/fact(i)
    
    return sum

print(series(3,4))


