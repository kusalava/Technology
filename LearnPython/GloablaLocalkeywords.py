x=100
y="asdfghjkl"
z=""
def asd():
    global x
    global y
    x = x*2
    y = y*8
    print(x)
    print(y)

def foo():
    global z
    z = "local"
    print(z)

def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()

foo()
print(z)
asd()
print(x)