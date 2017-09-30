# 返回函数：把函数作为返回值返回 也叫闭包
def return_func(*args):
	print(args)
	def calc():
		ax = 0
		for n in args:
			ax = ax + n
		return ax

	return calc

f1 = return_func(1,2,3,4,5)
f2 = return_func(1,2,3,4,5)

print(f1())
print(f2())
# 当调用return_func时 每次都会返回一个新的函数 即使参数一样 也是如此
print(f1 == f2) # false 

# 返回的函数并没有立刻执行，而是直到调用了f()才执行

def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1()) # 9
print(f2()) # 9
print(f3()) # 9

# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量

# 在内部把返回方法給执行了
def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs

print(f1()) # 1
print(f2()) # 4
print(f3()) # 9

# 匿名函数
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])) 