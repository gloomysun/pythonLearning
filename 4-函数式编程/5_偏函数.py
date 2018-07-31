print(int('8',base=9))
print(int('111',6))
print(int('111',2))

import functools
max2 = functools.partial(max, 10)
print(max2(1,2,3))


