#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 生成器
# 生成式的[] 改成() 就变成了生成器
# generator保存的是算法 不是具体的实体
# 如果一个函数定义中包含yield关键字 那么这个函数就是一个generator

g = (x * x for x in range(1, 11))

print(g)

for x in g:
	print(x)

# 斐波拉契数列 除第一个和第二个数外，任意一个数都可由前两个数相加得到
def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		# print(b)
		yield b
		a, b = b, a + b # 解构赋值 a = b b = a + b
		n = n + 1
	return 'done'

g1 = fib(6) # 1 1 2 3 5 8

for n in g1:
	print(n) # 1 1 2 3 5 8


# 杨辉三角算法
def triangles():
	L = [1]
	while True:
		yield L
		L.append(0)
		L = [L[i-1] + L[i] for i in range(len(L))]

i = 0
for t in triangles():
	print(t)
	i = i + 1
	if i == 10:
		break