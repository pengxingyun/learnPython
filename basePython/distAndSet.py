#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# dist python名字叫字典 javascript叫对象 以键-值对存储内容

d = {'aaa': 1, 'bbb': 2, 'sss': 3}

name = 'sss'
# 先判断key是否存在
if name in d:
	print(d[name])
	d.pop(name)
else: 
	print('没有找到%s' % name)

# 先判断key是否存在 0是d不存在name时返回的值
if d.get(name, 0):
	print(d[name])
	d.pop(name)
else: 
	print('没有找到%s' % name)


print(d)


# set 是一组key的集合 没有重复值
# 要创建一个set，需要提供一个list作为输入集合
s = set([1, 1, 2, 2, 3, 3])
print(s) # {1,2,3} // 重复值会被过滤

# s.add() 添加元素 重复添加不会有效果
s.add(4)
print(s) # {1,2,3,4} 

# remove() 删除元素
s.remove(4) 
print(s) # {1,2,3} 


# set可以做数学上的交并集操作

s1 = set([1,2,3])
s2 = set([2,3,4])

print(s1 & s2) # {2, 3} 取交集
print(s1 | s2) # {1, 2, 3, 4} 取并集

