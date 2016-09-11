#!usr/bin/env python3
#_*_ coding: utf-8 _*_

'a  test class';

__author__ = 'Jacky Yuan';

class Animal(object):
	"""docstring for Animal"""
	# def __init__(self, arg):
	# 	super(Animal, self).__init__()
	# 	self.arg = arg
	name = "Animal";
	def run(self):
		print("Animal is running...");


class Dog(Animal):
	def run(self):
		print("Dog is running...");
	
	def eat():
		print("Eating sometinog...");
		
class Cat(Animal):
	def run(self):
		print("Cat is running...");

dog = Dog();
dog.run();

cat = Cat();
cat.run();

print(isinstance(dog, (Dog, Animal)));
print("-----------");

import types;
print(type(dog.run()) == types.FunctionType);

dog.name = 'Dog';
print(dog.name == Animal.name);#对象属性并不会修改类属性的值
