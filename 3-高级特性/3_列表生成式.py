print(list(range(1, 11)))

s = [x * x for x in list(range(1, 10))]
print(type(s))
s = (x * x for x in list(range(1, 10)))
print(type(s))


s1 = [x * x for x in list(range(1, 10)) if x % 2 == 0]
print(s1)

s2 = [x + y + z for x in 'abc' for y in 'def' for z in 'ghi']
print(s2)

import os

print([d for d in os.listdir()])
print('====================练习=====================')
L1 = ['Hello', 'World', 18, 'Apple', None]

L2 = [x.lower() for x in L1 if isinstance(x,str)]
print(L2)