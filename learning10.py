#!usr/bin/env python3
#_*_ coding: utf-8 _*_

"a  test class";

__author__ = "Jacky Yuan";


#多继承

#由于Python允许使用多重继承，因此，MixIn就是一种常见的设计。
#只允许单一继承的语言（如Java）不能使用MixIn的设计。

#基类
class Animal(object):
	pass

#哺乳动物
class Mammal(Animal):
	pass

#蛋类动物
class Bird(Animal):
	pass

class Dog(Mammal):
	pass

class Parrot(Bird):
	pass

class Ostrich(Bird):
	pass


class Runnable(object):
	def run(self):
		print("Running...");

class Flyable(object):
	def fly(self):
		print("Flying...");

#蝙蝠,哺乳动物并且会飞
class Bat(Mammal, Flyable):
	pass

bat = Bat();
print(bat.fly());

#在设计类的继承关系时，通常，主线都是单一继承下来的，
#例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，
#通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，
#再同时继承Runnable。 这种设计通常称之为MixIn。