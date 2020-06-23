import random
import os, time
from multiprocessing import Process, Lock


def run(name):
    print('%s runing' % name)
    time.sleep(random.randrange(1, 5))
    print('%s running end' % name)


def demo():
    p1 = Process(target=run, args=('a',))  # 必须加,号
    p2 = Process(target=run, args=('b',))
    p3 = Process(target=run, args=('c',))
    p4 = Process(target=run, args=('d',))
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    print('主线程')


def no_lock_work():
    print('%s is running' % os.getpid())
    time.sleep(2)
    print('%s is done' % os.getpid())


def lock_work(lock):
    lock.acquire()
    print('%s is running' % os.getpid())
    time.sleep(2)
    print('%s is done' % os.getpid())
    lock.release()

# 不带锁
def no_lock():
    for i in range(3):
        p = Process(target=no_lock_work)
        p.start()

# 带锁
def lock():
    lock = Lock()
    for i in range(3):
        p = Process(target=lock_work, args=(lock,))
        p.start()


if __name__ == '__main__':
    demo()
    # no_lock()
    # lock()
