# sum = 0
# for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
#     sum = sum + x
# print(sum)


# print(list(range(5)))

# sum = 0
# for x in range(10):
#     sum = sum + x
# print(sum)

# sum = 0
# n = 10
# while n > 0:
#     sum = sum + n
#     n = n - 2
# print(sum)


# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# d['Tracy'] = 100;
# print(d['Tracy'])
# print('A' in d)
# print(d.get('A', "abc"))
# d.pop('Tracy')
# print(d.get('Tracy'))

# s = set([1, 1, 2, 2, 3, 3]);
# print(s);


# def calcu(n):
# 	sum = 0;
# 	for x in range(n):
# 	    sum = sum + x;
# 	return sum;

# def calcu2(n):
# 	sum = 0;
# 	while n > 0:
# 		sum =  n + sum;
# 		n -= 1;
# 	return sum;

# print(calcu2(6));

# def my_abs(x):
# 	if not isinstance(x,(int,float)):
# 		raise TypeError("bad argument type");
# 	if x >= 0:
# 		return x;
# 	else :
# 		return -x;

# import math
# def move(x, y, step, angle):
# 	nx = x + step * math.cos(angle);
# 	ny = y - step * math.sin(angle);
# 	return nx, ny;

# x, y = move(100, 100, 60, 30);
# r = move(100, 100, 60, 30);
# print(x, y , r);

# 一元二次方程求解 ax2 + bx + c = 0
import math
def quadratic(a, b, c):
	if (not isinstance(a,(int)) 
		or not isinstance(b,(int)) 
		or not isinstance(c,(int))):
	  raise TypeError("参数错误");
	if (a == 0):
		if b != 0:
			return -c / b;
		else :
			return "无解!";
	else :
		temp = b * b - 4 * a * c;
		if(temp >= 0):
			x1 = (-b + math.sqrt(temp)) / (2 * a);
			x2 = (-b + math.sqrt(temp)) / (2 * a);
			return x1, x2;
		else :
			return "无解!";

#默认参数
def power(x, n = 2):
    s = 1;
    while n > 0:
        n = n - 1;
        s = s * x;
    return s;
	
def add_end(l = None):
	if l is None:
		l = [];
	l.append('end');
	return l;

def calc(*number):
	sum = 0;
	for n in number:
		sum += n * n;
	return sum;

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

def fact(n):
	if n == 1:
		return 1;
	return n * fact(n - 1);

def fact1(n):
	return fact_iter(n,1);
def fact_iter(num,product):
	if num == 1:
		return product;
	return fact_iter(num - 1, num * product);
