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
