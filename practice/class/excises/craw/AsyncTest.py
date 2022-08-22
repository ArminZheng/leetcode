import asyncio
import time


async def read_file():
    # time.sleep(0.1)
    print("initial await asyncio.sleep(2.1)")
    await asyncio.sleep(2)
    print("await asyncio.sleep(2)")
    time.sleep(10)
    await asyncio.sleep(0.1)
    print("await asyncio.sleep(0.1)")
    return "file result"


async def read_api():
    # time.sleep(0.2)
    print("initial await asyncio.sleep(2)")
    await asyncio.sleep(2)
    print("second await asyncio.sleep(2)")
    return "api result"


async def read_db():
    # time.sleep(0.3)
    print("initial await asyncio.sleep(3)")
    await asyncio.sleep(3)  # 到达await关键字，发生上下文切换
    print("await asyncio.sleep(3)")
    return "db result"


async def main():
    await read_file()  # 不使用 await 函数不会暂定现场，不会再回到该调用点
    await read_api()
    await read_db()


async def gather():
    await asyncio.gather(
        asyncio.create_task(read_file()),
        asyncio.create_task(read_api()),
        asyncio.create_task(read_db()))


if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.run(gather())
