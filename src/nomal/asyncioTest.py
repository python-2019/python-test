import asyncio
import time


# https://www.cnblogs.com/ygbh/p/12015664.html  17  19
async def teach_student_async(n, t):
    print("开始辅导学生 %d  。。。" % n)
    await asyncio.sleep(t)
    print("学生 %d  结束辅导" % n)

# 协程加锁
async def teach_student_async_lock(n, t, lock):
    await lock.acquire()
    print("开锁辅导学生%d ...." % n)
    await asyncio.sleep(t)
    print("解锁学生 %d  辅导完成一半" % n)
    lock.release()


def teach_student(n, t):
    print("开始辅导学生 %d  。。。" % n)
    time.sleep(t)
    print("学生 %d  结束辅导" % n)


def asyncDemo():
    start = time.time()
    t1 = teach_student_async(1, 2)
    t2 = teach_student_async(2, 1)
    t3 = teach_student_async(3, 3)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(t1, t2, t3))
    loop.close()
    end = time.time()
    print("执行总时间：", end - start)


def asyncLockDemo():
    lock = asyncio.Lock()
    start = time.time()
    t1 = teach_student_async_lock(1, 2, lock)
    t2 = teach_student_async_lock(2, 1, lock)
    t3 = teach_student_async_lock(3, 3, lock)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.gather(t1, t2, t3))
    loop.close()
    end = time.time()
    print("执行总时间：", end - start)


def no_asyncDemo():
    start = time.time()
    teach_student(1, 2)
    teach_student(2, 1)
    teach_student(3, 3)
    end = time.time()
    print("执行总时间：", end - start)


if __name__ == '__main__':
    # asyncDemo()
    # no_asyncDemo()
    asyncLockDemo()
