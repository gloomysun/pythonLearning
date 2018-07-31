from collections import Iterable,Iterator

print(isinstance([],Iterable))
print(isinstance('',Iterable))
print(isinstance((),Iterable))

print(isinstance((),Iterator))
print(isinstance((list(range(10))),Iterator))
s = (x * x for x in list(range(1, 10)))
print(isinstance(s,Iterator))

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(isinstance(iter(L),Iterator))
print(type(iter(L)))
