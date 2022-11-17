import requests
from bs4 import BeautifulSoup

urls = [
    f"https://www.cnblogs.com/sitehome/p/{page}"
    for page in range(1, 50 + 1)
]


def craw(url):
    r = requests.get(url)
    # print(url, len(r.text), r.status_code)
    return r.text


def parse(html):
    soup = BeautifulSoup(html, "html.parser")
    links = soup.find_all("a", class_="post-item-title") # 可迭代对象
    return [(link["href"], link.get_text()) for link in links] # 构造一页的所有标题和链接


if __name__ == '__main__':
    for result in parse(craw(urls[5 - 1])):
        print(result)
