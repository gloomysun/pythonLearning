print(sorted([3,1,2]))
def fn(x):
    return -x
print(sorted([3,1,2],key=fn))
print(sorted([3,1,2],reverse=True))

def f1(x):
    return x.lower()
print(sorted(['a','b','A','Z']))
print(sorted(['a','b','A','Z'],key=f1))
print(sorted(['a','b','A','Z'],key=lambda x:x.lower()))
print('===============================练习=======================')
#L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#请用sorted()对上述列表分别按名字排序：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)

def by_socre(t):
    return t[1]
L2 = sorted(L, key=by_socre,reverse=True)
print(L2)