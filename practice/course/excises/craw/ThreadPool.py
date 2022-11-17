"""线程池
线程的生命周期:
「新建」- start 「就绪」
                        - 获得cpu资源 「运行」 - 失去cpu资源 「就绪」
                        - 获得cpu资源 「运行」 - sleep/io 「阻塞」 - sleep/io结束 「就绪」
                        - 获得cpu资源 「运行」 - run方法执行完 「终止」
线程池原理:
「新建」线程 系统需要分配资源; 终止线程系统需要回收资源.
如果可以重用x
"""

import concurrent.futures
import time

import blog_spider

"""使用线程池的两种方式
方式一: pool.map 模式
方式二: pool.submit + 循环 模式
"""
with concurrent.futures.ThreadPoolExecutor() as pool:
    htmls = pool.map(blog_spider.craw, blog_spider.urls)  # 优点: 简洁, 缺点: 1. 不能随时提交任务, 必须先把任务列表提前准备好 2. 返回是按顺序返回的
    htmls = list(zip(blog_spider.urls, htmls))
    # 按照顺序返回
    for url, html in htmls:
        print(url, len(html))

print("craw over")

with concurrent.futures.ThreadPoolExecutor() as pool:
    futures = {}
    for url, html in htmls:
        future = pool.submit(blog_spider.parse, html)  # 优点: 单个提交, 更加强大; 可以 1. 按顺序返回, 2. 哪个先结束 哪个先返回
        futures[future] = url

    start = time.time()

    # 两种获取结果方式
    # 饱汉式  ## 耗时 0.494758 s
    # for future, url in futures.items():
    # print(url, len(future.result()))

    # 饥汉式 ## 耗时 0.817104 s
    for future in concurrent.futures.as_completed(futures): # for in futures == for in futures.keys()
        url = futures[future]
        print(url, len(future.result()))
        
    for item in futures:
        print(item)

    print("## 耗时 %f %s" % (time.time() - start, "s"))
