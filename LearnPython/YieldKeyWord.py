def generator():
    for i in range(6):
        yield i*i
    

g = generator()
print(g)
print(type(g))
for i in g:
    print(i)