#切片
L = list(range(100));
print(L[::10]);#每隔10个取
print(L[-10:]);#取倒数10个数

#迭代
D = {'a':'0', 'b':'1', 'c':'2', 'd':'3'};
for x in D.items():
	print(x);

from collections import Iterable;
print(isinstance(D,(Iterable)));


#循环，Python提供的enumerate可以提供索引
for i,value in enumerate(range(10)):
	print(i,value);



e = [m + n for m in 'ABC' for n in 'XYZ'];
print(e);

#generator生成器
#在循环过程中不断调用yield，就会不断中断。
#当然要给循环设置一个条件来退出循环，不然就会产生一个无限数列出来。
def fib(max):
	n, a, b = 0, 0, 1;
	while n < max:
		#print(a);
		yield a;
		a, b = b, b + a;
		n += 1;
	return "done"

#odd不是普通函数，而是generator，在执行过程中，遇到yield就中断，下次又继续执行。
#执行3次yield后，已经没有yield可以执行了，所以，第4次调用next(o)就报错。
def odd():
	print("step 1");
	yield 1;
	print("step 2");
	yield 2;
	print("step 3");
	yield 3
	
#for 循环调用generator时获取不到返回值，
#要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中。
print('--------------');
g = fib(6);
while True:
	try:
		x = next(g);
		print("g", x);
	except StopIteration as e:
		print('Generator return value:', e.value);
		break;

#迭代器
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。
# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
print('--------------');
from collections import Iterator;
print(isinstance((x * x for x in range(10)),Iterator));
print(isinstance([],Iterator));
print(isinstance((),Iterator));
print(isinstance({},Iterator));
print(isinstance(iter([]),Iterator));


# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的.

for x in [1, 2, 3, 4, 5]:
    pass

#这两段代码等价。

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break