# try:
# 	f = open('test.txt', 'r')

# 	print(f.read())

# 	f.close()
# except IOError as e:
# 	raise e
# finally:
# 	if f:
# 		f.close()


with open('test.txt', 'r') as f:
	# 一次读取文件的全部内容
	# print(f.read())
	for line in f.readlines(): # 通常用于读取配置文件
		print(line.strip()) # 把末尾的'\n'删掉

# 打开二进制文件 图片 视频等
with open('/Users/pengxingyun/Downloads/myDear.jpeg', 'rb') as f:
	print(f.read())

# 指定文件的编码方式
with open('test.txt', 'r', encoding='UTF-8') as f:
	print(f.read())

# 编码不规范的文件 读取到错误内容-忽略
with open('test.txt', 'r', encoding='UTF-8', errors='ignore') as f:
	print(f.read())

# 写入内容 wb是写入二进制数据
with open('test.txt', 'w') as f:
	f.write('Hello world!')