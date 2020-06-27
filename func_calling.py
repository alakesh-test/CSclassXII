def A(x):
    print("the  value is",x)
    x=x+1
    if x==10:
        return x
    else:
        A(x)

# __ MAIN__

value=A(4)
print(value)