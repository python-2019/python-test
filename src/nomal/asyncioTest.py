import asyncio
import time


async def teach_student_async(n, t):
    print("开始辅导学生 %d  。。。" % n)
    await asyncio.sleep(t)
    print("学生 %d  结束辅导" % n)

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


def no_asyncDemo():
    start = time.time()
    teach_student(1, 2)
    teach_student(2, 1)
    teach_student(3, 3)
    end = time.time()
    print("执行总时间：", end - start)


if __name__ == '__main__':
    asyncDemo()
    # no_asyncDemo()