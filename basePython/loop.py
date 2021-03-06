#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# for...in 把list或tuple的每个元素迭代出来
names = ['aaa', 'bbbb', 'ccccc']

for x in names:
	print(x)

# range函数生成一个0-100的整数序列 不包括100
L = range(100)
# 通过list()转化为list
print(list(L))

# 计算1-100的整数之和
sum = 0
for x in range(101):
	sum = sum + x

print(sum)


# while 循环 只要条件满足，就不断循环，条件不满足时退出循环

# 计算100以内所有奇数之和

sum = 0
n = 99
while n > 0:
	sum = sum + n
	n = n - 2

print(sum)


# break 提前结束循环
n = 1
while n <= 100:
    if n > 10: # 当n = 11时，条件满足，执行break语句
        break # break语句会结束当前循环
    print(n)
    n = n + 1
print('END')

# continue 跳过本次循环 进入下次循环

n = 0
while n < 10:
    n = n + 1
    if n % 2 == 0: # 如果n是偶数，执行continue语句
        continue # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n)