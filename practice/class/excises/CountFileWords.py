def countWord():
    file_name = "README.md"
    key_words = "go"
    with open(file_name, "r", encoding="UTF-8") as f:
        sumword = f.read()
    print(sumword)
    if key_words in sumword:
        print(sumword.count(key_words))
    else:
        print("haven't")

countWord()

# 后台偷偷打上标记, 带上标记去到商品页的时候, 就能看到不同的价格了

# 起异步线程去写

