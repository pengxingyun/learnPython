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