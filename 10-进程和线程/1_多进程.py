# Unix/Linux操作系统提供了一个fork()系统调用，它非常特殊。
# 普通的函数调用，调用一次，返回一次，但是fork()调用一次，返回两次，
# 因为操作系统自动把当前进程（称为父进程）复制了一份（称为子进程），然后，分别在父进程和子进程内返回。

from multiprocessing import Process
import os


# 子进程要执行的代码
def run_proc(name):
    print('Run child process %s(%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s' % (os.getpid()))
    p = Process(target=run_proc, args=('test',))
    print('child process will start')
    p.start()
    p.join()
    print('child process end')

# Pool
# 如果要启动大量的子进程，可以使用进程池的方式批量创建子进程
from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds' % (name,end - start))


if __name__ == '__main__':
    print('Parent process %s' % os.getpid())
    p = Pool(5)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocess done...')
    p.close()
    p.join()
    print('All process done')
