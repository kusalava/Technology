import random
print(random.randrange(10,30))

x = ['a',1,2,3,'d','lef',3,[1,2,3,4,5,6,7,8]]
print(random.choice(x))
random.shuffle(x)
print(x)
