#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable
# 迭代
# 迭代一个对象
d = {'a': 1, 'b': 2, 'c': 3}

# 迭代key
for k in d:
	print(k) # abc 顺序不可控制 也可能是acb

# 迭代值
for v in d.values():
	print(v) # 123 顺序不可控制 也可能是132

for k in d:
	print(d[k]) # 123 顺序不可控制 也可能是132

# 键和值一起迭代
for k, v in d.items():
	print(k, v) # 123 顺序不可控制 也可能是132
	# a 1
	# b 2
	# c 3
	# 

# 判断一个值是否可迭代
print(isinstance([1,2,3], Iterable)) # Ture

# 对list实现下标循环
for i, value in enumerate(['A', 'B', 'C']):
	print(i, value)
	# 0 A
	# 1 B
	# 2 C

for x, y in [(1, 1), (2, 4), (3, 9)]:
	print(x, y)
	# 1 1
	# 2 4
	# 3 9