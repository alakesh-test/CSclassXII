# ####################################################
# Multipling two numbers using repeatative addition 
# 3 x 4= 3+3+3+3
# 3 x 4= 4+4+4
######################################################
'''
def multiply(x,n):
    m=0
    for i in range(x): # 0,1,2
        m+=n
    print(m)

multiply(3,4)
'''
# Recursivly

def multiply(x,n):
    if x==0:
        return n
    else:
        return n+multiply(x-1,n)
print(multiply(3,4))
