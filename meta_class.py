# -*- coding: utf-8 -*-

# Пример простого миксина

class AttributeInitType(type):
	"""asdas"""
	def __call__(self, *args, **kwargs):
		obj = type.__call__(self, *args)
		for name in kwargs:
			setattr(obj, name, kwargs[name])
		return obj

class Man(object):
	__metaclass__ = AttributeInitType

man = Man(height=180, weight=70)
print man.height
print man.weight


		
