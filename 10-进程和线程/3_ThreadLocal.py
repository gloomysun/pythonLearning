import threading

# 创建全局ThreaLocal对象
local_school = threading.local()


def process_student():
    # 获取当前线程关联的student
    std = local_school.student
    print('hello,%s (in %s)' % (std, threading.currentThread().name))

def process_thread(name):
    local_school.student = name
    process_student()

if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread,args=('zhangsan',))
    t2 = threading.Thread(target=process_thread,args=('lisi',))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    