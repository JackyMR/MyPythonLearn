#!usr/bin/env python3
#_*_ coding: utf-8 _*_

"a  test class";

__author__ = "Jacky Yuan";

# print

# 断言 assert 
def foo(s):
    n = int(s);
    assert n != 0, 'n is zero!';
    return 10 / n;

def main():
    foo('0');

# assert的意思是，表达式n != 0应该是True，
# 否则，根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError：
# Traceback (most recent call last):
#   ...
# AssertionError: n is zero!

# logging
import logging;
logging.basicConfig(level=logging.INFO);

s = '0';
n = int(s);
logging.info('n = %d' % n);
print(10 / n);

# pdb  Python的调试器

# IDE 如果要比较爽地设置断点、单步执行，
# 就需要一个支持调试功能的IDE。目前比较好的Python IDE有PyCharm。