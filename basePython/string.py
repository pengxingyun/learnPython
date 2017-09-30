#!/usr/bin/env python3 
# 在mac上面使用 可以直接执行./xxx.py

# 计算机只能处理数字，所以在计算机中所有需要处理的文本都是转换成数字处理


# ASCII编码 =================================> Unicode编码
#    ||                                           ||
# 基类只包含字符								  	  || 
#	 ||											  ||
# 导致每个国家只是在							把所有语言都统一到一套编码里
# 她的基础上添加自己						    解决乱码问题
# 国家的语言字符 出现乱码问题
# ASCII编码是1个字节，而Unicode编码通常是2个字节 所以如果写的文本都是英文的话 unicode会多一半的存储空间
# 							||
# utf-8 -------------  可变长编码 
# UTF-8编码把一个Unicode字符根据不同的数字大小编码成1-6个字节，常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节


# ord(str)获取单个字符的整数表示
print(ord('A'))
print(ord('中'))

# chr()函数把编码转换为对应的字符
print(chr(66))
print(chr(20016))

# 如果知道字符的整数编码，还可以用十六进制这么写str
print('\u767E\u5EA6')	# 百度

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
x = b'ABC'

# encode() 把Unicode表示的str编码为指定的bytes

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
# print('中文'.encode('ascii'))

# decode() 把bytes变为str
print(b'ABC'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# len()用来计算str包含多少个字符和bytes的字节数
print(len('ABC'))
print(len(b'ABC'))

# %运算符就是用来格式化字符串的

# %s 字符串
print('hello, %s', % 'world')

# %d 整数
print('hello, %d', % 1)

# %f 浮点型
print('hello, %f', % 1.1)

# %% 表示转义一个正常的%
print('hello, %%')








