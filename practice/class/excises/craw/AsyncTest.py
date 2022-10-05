import asyncio
import time


async def read_file():
    # time.sleep(5)
    print("initial read_file asyncio.sleep(2 + 3)")
    await asyncio.sleep(3)
    print("read_file 1/2 await asyncio.sleep(2)")
    # time.sleep(10)
    await asyncio.sleep(3)
    print("read_file 2/2 await asyncio.sleep(3)")
    return "file result"


async def read_api():
    # time.sleep(0.2)
    print("initial read_api await asyncio.sleep(2)")
    await asyncio.sleep(2)
    print("read_api whole await asyncio.sleep(2)")
    return "api result"


async def read_db():
    # time.sleep(0.3)
    print("initial read_db await asyncio.sleep(3)")
    await asyncio.sleep(3)  # 到达await关键字，发生上下文切换
    print("read_db whole await asyncio.sleep(3)")
    return "db result"


async def main():
    """asyncio.run(main())
    initial read_file asyncio.sleep(2.1)
    read_file 1/2 await asyncio.sleep(2)
    read_file 2/2 await asyncio.sleep(0.1)
    会阻塞
    initial read_api await asyncio.sleep(2)
    read_api whole await asyncio.sleep(2)
    第二次, 会阻塞
    initial read_db await asyncio.sleep(3)
    read_db whole await asyncio.sleep(3)
    """
    await read_file()  # 不使用 await 函数不会暂定现场，不会再回到该调用点
    print("会阻塞")
    await read_api()
    print("第二次, 会阻塞")
    await read_db()


async def gather():
    """asyncio.run(gather())
    initial read_file asyncio.sleep(2.1)
    initial read_api await asyncio.sleep(2)
    initial read_db await asyncio.sleep(3)
    read_file 1/2 await asyncio.sleep(2)
    read_api whole await asyncio.sleep(2)
    read_db whole await asyncio.sleep(3)
    read_file 2/2 await asyncio.sleep(0.1)
    """
    await asyncio.gather(
        asyncio.create_task(read_file()),
        asyncio.create_task(read_api()),
        asyncio.create_task(read_db()))


if __name__ == '__main__':
    # asyncio.run(main())
    asyncio.run(gather())
