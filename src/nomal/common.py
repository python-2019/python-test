import asyncio
import time

# 开头定义async,表示要在协程运行，不定义的话，循环监听增加不了
async def coroutine():
    print("协程运行")
    print("运行结束")


if __name__ == '__main__':
    # 定义一个事件循环监听
    event_loop = asyncio.get_event_loop()
    print('协程开始...')
    coroutine_1 = coroutine()
    coroutine_2 = coroutine()
    coroutine_3 = coroutine()
    print('进入事件循环监听...')
    # run_until_complete翻译成中文：一直运行到完成为止
    event_loop.run_until_complete(coroutine())
    print('关闭事件循环监听..')
    event_loop.close()