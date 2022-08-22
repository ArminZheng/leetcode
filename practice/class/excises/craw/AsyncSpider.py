import asyncio
import time
import aiohttp
import blog_spider

semaphore = asyncio.Semaphore(10)


async def async_craw(url):
    async with semaphore:
        print("craw url: ", url)
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                result = await resp.text()
                await asyncio.sleep(2)
                print(f"craw url: {url}, {len(result)}")

loop = asyncio.get_event_loop()

tasks = [loop.create_task(async_craw(url))
         for url in blog_spider.urls]

start = time.time()
# 单线程异步爬虫, 很多时候是快于多线程的
loop.run_until_complete(asyncio.wait(tasks))
print('## 耗时 %f %s' % (time.time() - start, 's')) # 0.259786 s
