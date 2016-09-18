#!usr/bin/env python3
#_*_ coding: utf-8 _*_

"a  test class";

__author__ = "Jacky Yuan";

#Custom Class 定制类

#__str__
#只需要定义好__str__()方法,就可打印出实例对象
class Student(object):
	"""docstring for Student"""
	def __init__(self, name):
		self.name = name;

	def __str__(self):
		return "Student Object (name : %s)" % self.name;

s = Student("JACKY")
print(s);
		
#__iter__
class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		self.a, self.b = 0, 1;

	def __iter__(self):
		return self;

	def __next__(self):
		self.a, self.b = self.b, self.a + self.b;
		if(self.a > 10000):
			raise StopIteration();
		return self.a;

	def __getitem__(self, n):
		if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

for n in Fib():
	print(n);


f = Fib();
print(f[100]);

#__setitem__
#__getattr__
#__call__