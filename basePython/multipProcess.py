# 多CPU多任务是并行，单核多任务是并发

# 多进程

# import os

# print('Process (%s) start...' % os.getpid())

# # Only works mac
# pid = os.fork()
# if pid == 0:
# 	print('I`m child Process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
# else:
# 	print('I (%s) just created a child process (%s).' % (os.getpid(), pid))


# window下创建多进程
# 创建一个Process实例 用start()方法启动
# from multiprocessing import Process
# import os

# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join() #join方法等待子进程结束后再往下运行 用于进程之间的同步
#     print('Child process end.')


# 用进程池Pool的方式批量创建子进程
# from multiprocessing import Pool
# import os, time, random

# def long_time_task(name):
#     print('Run task %s (%s)...' % (name, os.getpid()))
#     start = time.time()
#     time.sleep(random.random() * 3)
#     end = time.time()
#     print('Task %s runs %0.2f seconds.' % (name, (end - start)))

# if __name__=='__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Pool(4)
#     for i in range(5):
#         p.apply_async(long_time_task, args=(i,))
#     print('Waiting for all subprocesses done...')
#     p.close()
#     p.join()
#     print('All subprocesses done.')



# subprocess
import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)