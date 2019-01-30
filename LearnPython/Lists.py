pow2 = [2 ** x for x in range(10) if x > 5]
print(pow2)
odd = [x for x in range(20) if x % 2 == 1]
print(odd)
z = [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
print(z)