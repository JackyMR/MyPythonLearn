# 高阶函数
def add(x, y, f):
	return f(x) + f(y);
print(add(-1, -2, abs));

# map/reduce
def f(x):
	return x * x;

mylist = list(range(10));
r = map(f, mylist);
print(list(r));
print(list(map(str, mylist)))

# 1,3,5,7,9 -> 13579
from functools import reduce
def add2(x, y):
	return x * 10 + y;
print(reduce(add2, list(range(1, 11))[::2]));


#filter
def not_empty(s):
	return s and s.strip();
a = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']));
print(a);

#筛选素数
def odd_iter():
    n = 1;
    while True:
        n = n + 2;
        yield n;

def not_divisible(n):
	return lambda x: x % n > 0;

def primess():
	yield 2;
	it = odd_iter();
	while True:
		n = next(it);
		yield n;
		it = filter(not_divisible(n), it)

for n in primess():
	if(n < 1000):
		print(n)
	else:
		break;

#sort
print(sorted([2, -20, 10, -80]));
print(sorted([36, 5, -12, 9, -21], key = abs));
print(sorted(['bob', 'about', 'Zoo', 'Credit']));#ascii排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse = True));


L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

def by_name(t):
    return t[0][:1].upper();

print(sorted(L, key = by_name));

def by_score(t):
    return int(t[1]);

print(sorted(L, key = by_score));






