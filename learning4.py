
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



def log(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__);
        return func(*args, **kw);
    return wrapper;

@log
def now():
	print('2016-09-10')