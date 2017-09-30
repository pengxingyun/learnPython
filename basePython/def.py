#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0
# 的两个解。

import math

def quadratic(a = 2, b = 3, c = 1):
	x1 = (math.sqrt(b * b - 4 * a * c) - b) / (2 * a)
	x2 = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
	return x1, x2

def aa():
	return 2;

print(quadratic()) # 默认参数必须指向不变对象
print(quadratic(2, 3, 1)) # (-0.5, -1.0) 返回值是一个元组
print(quadratic(1, 3, -4)) # (1.0, -4.0) 返回值是一个元组
t = aa()
print(t)




# 默认参数
# 当没有传入n参数时 n = 2
def power(x, n=2):
	s = 1
	while n > 0:
		n = n - 1
		s = s * x

	return s

print(power(2, 3)) # 8
# 参数的顺序不受限制 但是需要注明参数的对应值
print(power(n=3, x=2)) # 8

# 可变函数 or 扩展函数 原理:把参数当做一个list或者tuple
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum += n
	return sum

print(calc(1,2,3,4)) # 10 

# 如果已经有一个list或者tuple 要调用一个可变参数 可以把list或tuple的元素变成可变参数传进去
num = [1, 2, 3]
print(calc(*num)) # 6

# 关键字参数 
def person(name, age, **kw):
	# kw在函数内其实是一个dict 函数调用时除了name, age两个必选参数 其他都是kw里面的键值对
	print('name', name, 'age', age, 'other', kw)

person('xingyunn', 22, city='guangzhou', job='programmer')
# name xingyunn age 22 other {'job': 'programmer', 'city': 'guangzhou'}
# 也可以把已定义的dict转换成关键字参数传入
obj = {'city': 'guangzhou', 'job': 'programmer'}
person('xingyunn', 22, **obj) #name xingyunn age 22 other {'job': 'programmer', 'city': 'guangzhou'}


# 命名关键字函数
# 只接收city和job作为关键字参数
def person1(name, age, *, city, job):
	print(name, age, city, job)

person1('Jack', 24, city='Beijing', job='Engineer') # Jack 24 Beijing Engineer
# 命名关键字函数必须传入参数名 否则会报错 person1只接受2个位置参数 但传入了4个
# person1('Jack', 24, 'Beijing', 'Engineer') # TypeError: person1() takes 2 positional arguments but 4 were given

# 如果函数定义中已经有了一个可变参数 后面的命名关键字不需要*特殊分割符 
# 命名关键字函数也可以有缺省值 默认参数
def person2(name, age, *args, city='Beijing', job):
	print(name, age, city, job)

person2('Jack', 24, city='Beijing', job='Engineer') # Jack 24 Beijing Engineer