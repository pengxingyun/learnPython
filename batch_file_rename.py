# batch_file_rename.py
# Create: 2017-10-12

'''
批量修改给出的目录里面后缀名符合的文件的后缀名
比如把指定目录的.txt文件修改为.py文件
'''

__author__ = 'pengxingyun'

__version__ = '1.0'

# argparse用来获取命令行的输入 sys.argv的更高级做法
import os,argparse

default_dir = os.path.abspath('.')
def batch_rename(work_dir = default_dir, old_ext = '.txt', new_ext = '.py'):
	'''
	批量修改给出的目录里面后缀名符合的文件的后缀名
	'''
	for filename in os.listdir(work_dir):
		# splitext获取文件的后缀名 split是获取整个文件名
		split_file = os.path.splitext(filename)
		file_ext = split_file[1] # .py形式

		# 判断文件夹中与输入的后缀名符合的文件
		if old_ext == file_ext:
			newfile = split_file[0] + new_ext

			# 执行重命名
			os.rename(
					os.path.join(work_dir, filename),
					os.path.join(work_dir, newfile)
			)

def get_parser():
    parser = argparse.ArgumentParser(description='change extension of files in a working directory')
    parser.add_argument('work_dir', metavar='WORK_DIR', type=str, nargs=1, help='the directory where to change extension')
    parser.add_argument('old_ext', metavar='OLD_EXT', type=str, nargs=1, help='old extension')
    parser.add_argument('new_ext', metavar='NEW_EXT', type=str, nargs=1, help='new extension')
    return parser

def main():
	parser = get_parser()
	# python batch_file_rename.py ./ .txt .py
	# 返回一个dict {'new_ext': ['.py'], 'old_ext': ['.txt'], 'work_dir': ['./']}
	args = vars(parser.parse_args())
	
	work_dir = args['work_dir'][0]

	old_ext = args['old_ext'][0]

	new_ext = args['new_ext'][0]

	# 如果给定的后缀名不是以.开头 加上.再判断、修改
	if old_ext[0] != '.':
		old_ext = '.' + old_ext

	if new_ext[0] != '.':
		new_ext = '.' + new_ext

	batch_rename(work_dir, old_ext, new_ext)

if __name__ == '__main__':
	main()