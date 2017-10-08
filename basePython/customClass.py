# 定制类
# 用类实现斐波那契数列
# class Fib(object):
# 	def __init__(self):
# 		self.a, self.b = 0, 1
# 	def __iter__(self):
# 		return self
# 	def __getitem__(self, n):
# 		a, b = 1, 1
# 		for x in range(n):
# 			a, b = b, a + b
# 		return a
# 	def __next__(self):
# 		self.a, self.b = self.b, self.a + self.b
# 		if self.a > 100000:
# 			raise StopIteration()
# 		return self.a # 返回下一个值

# for n in Fib():
# 	print(n)
	
class Student(object):
		def __init__(self, name):
			self.name = name
		# __str__定制返回类的描述字段
		def __str__(self):
			return 'Student object (name: %s)' % self.name

		__repr = __str__

print(Student('pengxingyun'))
				