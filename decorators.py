# -*- coding: utf-8 -*-

# пример простого декоратора

def return_false():
	return false

def checkArgs(f):
	def wrapper(*args, **kwargs):
		for arg in args:
			if arg > 30:
				print u'хм... какое большое число. Ну нафиг его.'
				return 0
		return f(*args, **kwargs)
	return wrapper

def growParams(f):
	def wrapper(*args, **kwargs):
		return f(*tuple([x+10 for x in args]), **kwargs)
	return wrapper

@growParams
@checkArgs
def showSum(*args, **kwargs):
	arg_sum = 0
	for arg in args:
		arg_sum += arg
	return arg_sum

print showSum(1,2,30)
