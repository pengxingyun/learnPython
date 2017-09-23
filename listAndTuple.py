#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# list 有序集合类型 相当于数组Array
names = ['aaa', 'bbb', 'ccc']

print(names) # ['aaa', 'bbb', 'ccc']

# len 获取list元素个数
print(len(names))

# 索引访问list元素
print(names[0]) # 第一个
print(names[len(names) - 1]) # 最后一个
print(names[-1]) # 最后一个
print(names[-2]) # 倒数第二个

# 追加元素到末尾
names.append('ddd')
print(names) # ['aaa', 'bbb', 'ccc', 'ddd']

# 插入元素到指定位置
names.insert(1, 'insert1') 
print(names) # ['aaa', 'insert1', 'bbb', 'ccc', 'ddd']

# 删除list指定位置的元素 参数缺省为删除最后一位
names.pop(); # 删除最后一位
names.pop(1); # 删除第二位元素
print(names); # ['aaa', 'bbb', 'ccc']

# 修改元素 直接赋值给指定元素
names[1] = 'bbb'
print(names) # ['aaa', 'bbb', 'ccc']

# list里面的数据类型可以不同
L = ['aaa', 1, True]

# list里面也可以包含list
s = ['aaa', ['bb', 'cc'], True]

# 元组： tuple tuple一旦初始化不能修改

classmates = ('aaa', 'bbb', 'ccc') # 不可修改 

# 获取元素 classmates[0]
print(classmates[0])

# 定义只有一个元素的tuple时 需要加一个,消除歧义
t = (1,)

