# 面向对象编程
# 基础定义

class Student(object):
	def __init__(self, name='peng', score='99'): 
		# 实例的变量名如果以__开头 就变成了一个私有变量 外部不能访问
		self.__name = name
		self.__score = score

	# 外部需要访问name score 需定义getter setter方法
	def get_name(self):
		return self.__name

	def get_score(self):
		return self.__score

	def set_name(self, name):
		self.__name = name

	def set_score(self, score):
		self.__score = score

	def printScore(self):
		print("%s: %s" % (self.get_name(), self.get_score()))

bart = Student()

print(bart._Student__name)
print(bart.printScore())



# 继承 多态
# 父类
class Animal(object):
	def run(self):
		print('Animal is running...')

# 子类
# 继承的最大的好处是子类获得了父类的全部功能
# 多态就是子类可以根据继承来的属性重构自己独有的函数
class Dog(Animal):
	# 重写Animal的run方法
	def run(self):
		print('Dog is running...')
	# 添加Dog特有方法
	def eat(self):
		print('Eating meat...')

class Cat(Animal):
	# 重写Animal的run方法
	def run(self):
		print('Cat is running...')
		
		
d = Dog()
c = Cat()

d.run()
c.run()

# 使用type()判断对象类型
print(type(123))
print(type(d))
print(type(None))

# 使用isinstance()判断是否继承关系
print(isinstance(c, Animal)) # True

# 能用type()判断的基本类型也可以用isinstance()判断
print('---------',isinstance(123, int)) # True
print(isinstance(b'a', bytes)) # True

# dir()获得一个对象的所有属性和方法
import types
dir(types)

# len() __len__() 获取对象的长度
print(len('ABC')) # 3
print('ABC'.__len__()) # 3

# lower() 返回小写的字符串
print('ABC'.lower()) # abc

# getattr() setattr() hasattr() 操作一个对象的状态
print(hasattr(bart, '_Student__name')) # True
print(getattr(bart, '_Student__name', 404)) # peng 404 设置一个默认值 如果值不存在就返回默认值
