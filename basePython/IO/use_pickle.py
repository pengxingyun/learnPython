import pickle, io
from io import BytesIO
d = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d)) # dumps方法把任意对象序列化成一个bytes

with open('test.txt', 'wb') as f:
	f.write(pickle.dumps(d))
