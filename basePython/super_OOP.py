# 动态语言的面向对象编程 优势在于可以给创建的实例绑定任何属性和方法
class Student(object):
	# 对可以动态绑定的属性做个限制 只可以传入tuple内的元素
	__slots__ = ('name', 'age', 'set_age', 'score')
	# name = 'Student'
	def __init__(self, name='xingyun'):
		self.name = name
	# 改变print(Student())的打印内容
	def __str__(self):
		return 'Student object (name: %s)' % self.name
	__repr__ = __str__

	
print(Student()) # Student object (name: xingyun)
s = Student()
# 动态给实例绑定一个属性
s.name = 'xingyun' 
print(s.name) # xingyun

# 动态给实例绑定一个方法
def set_age(self, age):
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)
s.set_age(25)
print(s.age) 

# 但是，给一个实例绑定的方法，对另一个实例是不起作用的
# 我们可以直接给class绑定方法
def set_score(self, score):
	self.score = score

Student.set_score = set_score

s.set_score('99')
print(s.score)

# s.height = '175' # AttributeError: 'Student' object has no attribute 'height'

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的
class GraduateStudent(Student):
	pass

gs = GraduateStudent()
gs.score = '98' 
print(gs.score) # 98 没有__slot__ 等于不限制



# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
	# def __init__():
	# 	pass
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self, v):
		self._width = v

	@property
	def height(self):
		return self._width

	@width.setter
	def height(self, v):
		self._height = v

	@property
	def resolution(self):
		return self._width * self._height

s = Screen()
s.width = 1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution
		
		