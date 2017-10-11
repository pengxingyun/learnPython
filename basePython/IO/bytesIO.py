from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))

print(f.getvalue())

# 读取
print(f.read())