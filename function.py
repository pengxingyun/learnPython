
# 高阶函数： 一个函数就可以接收另一个函数作为参数
# map 实现f(x) = x * x
from functools import reduce
def f(x):
	return x * x

print(list(map(f, list(range(1, 10))))) # [1, 4, 9, 16, 25, 36, 49, 64, 81]
# list 转化为字符串
print(list(map(str, list(range(1, 10))))) # ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def str2int(s):
	def fn(x, y):
		return x * 10 + y
	def char2num(s):
		L = {}
		# 把[1,2,3,4,5,6,7,8,9] 转化为 {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
		for x in [str(x) for x in range(10)]:
			L[x] = int(x)
		return L[s]
	return reduce(fn, map(char2num, s))

print(str2int('12345'))
print(int('12345'))

# 把用户输入的不规范的英文名字，变为首字母大写
def normalize(name):
	return name.capitalize()


L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 用reduce求出数组中的乘积
def prod(L):
	return reduce(lambda x,y: x * y, L)

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

# 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456
# todo 有问题 inconsistent use of tabs and spaces in indentation

# def str2float(s):
# 	s = s.split('.')
# 	def f1(x,y):
#         return x * 10 + y

#     def f2(x,y):
#         return x / 10 + y

# 	def char2num(s):
# 		L = {}
# 		# 把[1,2,3,4,5,6,7,8,9] 转化为 {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
# 		for x in [str(x) for x in range(10)]:
# 			L[x] = int(x)
# 		return L[s]

# 	return reduce(f1,map(str2num,s[0])) + reduce(f2,list(map(str2num,s[1]))[::-1])/10

# print('str2float(\'123.456\') =', str2float('123.456'))

# filter() 筛选
# 回数是指从左向右读和从右向左读都是一样的数 原来把这个数倒过来相等就行了 -.-
def is_palindrome(n):
    b = int(str(n)[::-1])
    return b == n
output = filter(is_palindrome, range(1, 1000))
print(output)
print(list(output))

# sorted key=abs
def by_name(t):
	return t[0]

def by_score(t):
	return t[1]

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]

L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score, reverse=True)
print(L2)
print(L3)









