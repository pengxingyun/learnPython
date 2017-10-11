from io import StringIO
# 写入内存
f = StringIO()
f.write('hello')
f.write(' ')
f.write('world')
print(f.getvalue()) # getvalue()方法用于获得写入后的str

# 读取StringIO
while True:
	s = f.readline()
	if s == '':
		break
	print(s.strip())
