#!usr/bin/env python3
#_*_ coding: utf-8 _*_

"a  test class";

__author__ = "Jacky Yuan";

class Hello(object):
    def hello(self, name='world'):
        print('Hello, %s.' % name)

hello = Hello();
hello.hello();

print(type(Hello));
print(type(hello));

# type()函数可以查看一个类型或变量的类型，
# Hello是一个class，它的类型就是type，
# 而h是一个实例，它的类型就是class Hello。

