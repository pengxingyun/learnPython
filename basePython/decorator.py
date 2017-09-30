# 定义一个能打印日志的decorator
import functools

# 重写log 使他支持 @log @log(excute) 函数调用的前后打印出begin call 和 end call
def log(arg):
	if callable(arg):
		def wrapper(*args, **kw):
			print('begin call')
			print('call %s():' % (arg.__name__))
			a = arg(*args, **kw)
			print('end call')
			return a
		return wrapper
	else:
		def decorator(func):
			@functools.wraps(func)
			def wrapper(*args, **kw):
				print('begin call')
				print('%s %s():' % (arg, func.__name__))
				a = func(*args, **kw)
				print('end call')
				return a
			return wrapper
		return decorator


@log('excute')
def f1():
	print('test decorator text')

@log
def f2():
	print('test decorator')

f1()
f2()

# 偏函数
# 把一个函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单
# 把'12345'转成int 以八进制转换
print(int('12345', base=8))
#固定int2为2进制转换的int
int8 = functools.partial(int, base=8)

print(int8('12345'))