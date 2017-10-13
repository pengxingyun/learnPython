# batch_file_rename.py
# Create: 2017-10-12

'''
判断目录是否存在 不存在则创建
'''

import os 

MESSAGE = '目录已经存在'
TESTDIR = 'testdir'

try:
	# home  = os.path.expanduser("~") # 用来将包含～符号的路径扩展为完整的路径
	home = os.getcwd() # 获取当前目录
	print(home)

	if not os.path.exists(os.path.join(home, TESTDIR)):
		# os.mkdir = os.makedirs
		os.mkdir(os.path.join(home, TESTDIR))
	else:
		print(MESSAGE)
except Exception as e:
	raise e
finally:
	pass