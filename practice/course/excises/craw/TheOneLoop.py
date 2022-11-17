import asyncio

loop = asyncio.get_event_loop()

def get_url(url):
    pass
url = ""

async def myfunc(url):
    await get_url(url)

tasks = [loop.create_task(myfunc(url))]

loop.run_until_complete(asyncio.wait(tasks))