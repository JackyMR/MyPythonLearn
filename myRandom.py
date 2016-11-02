#!usr/bin/env python3
#_*_ coding: utf-8 _*_

__author__ = "Jacky Yuan";

import random

class Test(object):
	"""docstring for ClassName"""

	def access_random_phone(self, num):
		phone = '';
		for x in range(0, num):
			phone = phone + str(random.randrange(0, 10));
		return phone

var = Test();
print(var.access_random_phone(11))