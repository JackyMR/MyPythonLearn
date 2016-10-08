#!usr/bin/env python3
#_*_ coding: utf-8 _*_


try:
  f = open("c:/users/jacky/desktop/新建文本文档.txt", "r");
  print(f.read());
finally:
  if f:
    f.close();

with open("c:/users/jacky/desktop/新建文本文档.txt", "r") as f:
	print(f.read());

f = open("c:/users/jacky/desktop/新建文本文档.txt", "r");
for line in f.readline():
	print(line.strip());

f = open("c:/users/jacky/desktop/新建文本文档.txt", "rb");#二进制

f = open('/Users/michael/gbk.txt', 'r', encoding='gbk');