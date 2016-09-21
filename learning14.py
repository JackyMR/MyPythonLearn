#!usr/bin/env python3
#_*_ coding: utf-8 _*_

"a  test class";

__author__ = "Jacky Yuan";


try:
    print('try...');
    r = 10 / 0;
    print('result:', r);
except ZeroDivisionError as e:
    print('except:', e);
finally:
    print('finally...')
print('END');


try:
    print('try...');
    r = 10 / int('a');
    print('result:', r);
except ValueError as e:
    print('ValueError:', e);
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e);
finally:
    print('finally...');
print('END');


import logging;

def foo(s):
    return 10 / int(s);

def bar(s):
    return foo(s) * 2;

def main():
    try:
        bar('0');
    except Exception as e:
        logging.exception(e);

main();
print('END');

# 抛出错误
class FooError(ValueError):
	pass;

def foo(s):
	n = int(s);
	if n== 0:
		raise FooError("invalid value : %s" % s);
	return 10 / n;