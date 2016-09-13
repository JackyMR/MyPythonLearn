#!usr/bin/env python3
#_*_ coding: utf-8 _*_

'a  test class';

__author__ = 'Jacky Yuan';


# 使用__slots__
class Student(object):
	pass;

s = Student();
s.name = "JACKY";
print(s.name);


def set_age(self, age):
	self.age = age;

from types import MethodType;
s.set_age = MethodType(set_age, s);
s.set_age(25);
print(s.age)

s2 = Student();
#s2.set_age(25);

def set_score(self, score):
	self.score = score;

Student.set_score = set_score;
s.set_score(100);
print(s.score);

s2.set_score(90);
print(s2.score);

class Student2(object):
 	__slots__ = ("name", "age");

s = Student2();
s.name = "JACKY";
s.age = 24;
#s.score = 99;

class GraduateStu(Student2):
	pass

g = GraduateStu();
g.score = 99;


