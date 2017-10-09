class Hello(object):
	def hello(self, name='world'):
		print('Hello, %s.' % name)
		

# 命令行import文件-执行
# from metaClass import Hello
# h = Hello()
# h.hello()
# type()返回对象的类型
# print(type(Hello))
# print(type(h))

# type()创建新的类型

# def fn(self, name='world'):
# 	print('Hello, %s.' % name)

# Hello = type('Hello', (object,), dict(hello=fn)) # 创建Hello class

# h = Hello()

# h.hello()

# print(type(Hello))

# print(type(h))

# 要创建一个class对象，type()函数依次传入3个参数：

# 1. class的名称；
# 2. 继承的父类集合，注意Python支持多重继承，如果只有一个父类，别忘了tuple的单元素写法；
# 3. class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上。


# 先定义metaclass，就可以创建类，最后创建实例 把类看成是metaclass创建出来的“实例”

class ListMetaclass(object):
	def __new__(cls, name, bases, attrs):
		attrs['add'] = lambda self, value: self.append(value)
		return type.__new__(cls, name, bases, attrs)
