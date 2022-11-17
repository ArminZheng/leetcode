from typing import *
import blog_spider
import threading
from util.Util import timesum


@timesum
def single_thread():
    print("single_thread begin")
    for url in blog_spider.urls:
        blog_spider.craw(url)
    print("single_thread end")


@timesum
def multi_thread():
    print("mutil_thread begin")
    threads: List[threading.Thread] = []
    for url in blog_spider.urls:
        threads.append(
            threading.Thread(target=blog_spider.craw,
                             args=(url,))  # 不加逗号是个字符串, 而不是元祖
        )

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(threads.__len__())
    print("multi_thread end")


if __name__ == '__main__':
    single_thread() # 3.465031 s
    multi_thread() # 0.239491 s
