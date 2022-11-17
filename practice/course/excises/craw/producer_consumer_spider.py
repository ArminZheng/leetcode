from io import TextIOWrapper
from queue import Queue
import blog_spider
import time
import random
import threading


def do_craw(url_queue: Queue, html_queue: Queue):
    while True:
        url = url_queue.get() # 生产者拉取原料
        html = blog_spider.craw(url) # 生产中间数据
        html_queue.put(html) # 中间数据放入队列
        print(threading.current_thread().name,
              f"craw {url}", "剩余链接数 = ", url_queue.qsize())
        time.sleep(random.randint(1, 2))


def do_parse(html_queue: Queue, fout: TextIOWrapper):
    while True:
        html = html_queue.get() # 消费者拉去食物 (中间数据)
        results = blog_spider.parse(html)  # 消费中间数据得到产出: 得到一页有多少结果 result.len()
        for result in results:
            fout.write(str(result) + "\n")
        print(threading.current_thread().name,
              f"currentPage = {len(results)}, 有多少没拉取完 = {html_queue.qsize()}")
        # print(results)
        time.sleep(random.randint(1, 2))


if __name__ == '__main__':
    url_queue = Queue()
    html_queue = Queue()
    for url in blog_spider.urls:
        url_queue.put(url)

    for idx in range(3):
        t = threading.Thread(
            target=do_craw, args=(url_queue, html_queue), name=f">>> craw{idx}"
        )
        t.start()
    fout = open("02.data.txt", "w", encoding="UTF-8")
    for idx in range(2):
        t = threading.Thread(
            target=do_parse, args=(html_queue, fout), name=f"<<< parse{idx}"
        )
        t.start()
    print("开始了")
