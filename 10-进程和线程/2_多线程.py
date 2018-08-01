import time, threading


def loop():
    print('thread %s is running..' % threading.currentThread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>>%s' % (threading.currentThread().name, n))
        time.sleep(0.1)
    print('thread %s ended' % threading.currentThread().name)


print('thread %s is running...' % threading.currentThread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.currentThread().name)

balance = 0
lock = threading.Lock()

def change_it(n):
    global balance
    balance = balance + n
    balance = balance - n


def run_thread(n):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
