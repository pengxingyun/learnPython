import logging
logging.basicConfig(level=logging.INFO)
# 1. print
# def foo(s):
# 	n = int(s)
# 	print('>>> n = %d' % n)
# 	return 10 / n

# def main():
# 	foo('0')

# main()

# #2. assert 断言调试
# def foo(s):
#     n = int(s)
#     assert n != 0, 'n is zero!'
#     return 10 / n

# def main():
#     foo('0')

# 3. logging
import logging

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)