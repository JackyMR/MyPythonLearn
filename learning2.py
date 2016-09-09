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



