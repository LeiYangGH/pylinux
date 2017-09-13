def mul3(f):
    return lambda x:f(x)*3
    #def w(x):
    #    return f(x)*3
    #return w

@mul3
def pow2(x):
    return x*x

x=5
r=pow2(x)
print(r)
