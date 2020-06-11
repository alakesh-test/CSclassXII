x=10
def scope():
   return x

print("Value return by scope()",scope())
def scopeLocal():
    x=20
    print(x)

print("Value return by scopeLocal()",scopeLocal())
print("From __main__ printing x",x)