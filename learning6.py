#!usr/bin/env python3
#_*_ coding: utf-8 _*_

'a  test class';

__author__ = 'Jacky Yuan';

class Student(object):
	"""docstring for Student"""
	def __init__(self, name, score):
		super(Student, self).__init__();
		self.__name = name;
		self.__score = score;

	def print_score(self):
		print('%s: %s' % (self.__name, self.__score));

	def get_grade(self):
		if self.__score >= 90:
			return 'A';
		elif self.__score >= 80:
			return 'B';
		else:
			return 'C';

	def setScore(self, score):
		self.__score = score;

	def setName(self, name):
		self.__name = name;

	def get_name(self):
		return self.__name;

	def get_score(self):
		return self.__score;

bart = Student('Bart', 99);
lisa = Student('Lisa', 90);
bart.print_score();
print(bart._Student__name);#特殊方法获取对象的私有属性

lisa.print_score();
print(bart.get_grade(), lisa.get_grade());
print(bart.get_name());