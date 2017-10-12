import pickle, io, json
from io import BytesIO
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d)) # dumps方法把任意对象序列化成一个bytes

# 序列化 写入文件
with open('test.txt', 'wb') as f:
	f.write(pickle.dumps(d))

# 序列化读取文件
with open('test.txt', 'rb') as f:
	print(pickle.load(f))

