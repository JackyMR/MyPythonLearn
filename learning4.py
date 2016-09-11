
#返回函数

def lazy_sum(*args):
    def sum():
        ax = 0;
        for n in args:
            ax = ax + n;
        return ax;
    return sum;

f = lazy_sum(1, 3, 5, 7, 9);
print(f());
f2 = lazy_sum(1, 3, 5, 7, 9);
print(f == f2);
print(f() == f2());


#装饰器
def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__);
        return func(*args, **kw);
    return wrapper;

@log
def now():
	print('2016-09-10')

#偏函数

#默认转二进制方法
def int2(x, base = 2):
    return int(x, base);

#functools.partial就是帮助我们创建一个偏函数的，
#不需要我们自己定义int2()，
#可以直接使用下面的代码创建一个新的函数int2。
import functools;
int2 = functools.partial(int, base = 2);
print(int2('1000'));
print(int2('1000', base = 10));