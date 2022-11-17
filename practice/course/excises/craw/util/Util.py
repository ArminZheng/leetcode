from time import time


def timesum(fn):
    def inner(*args, **kwargs):
        print(">>开始计时!")
        start = time()
        result = fn(*args, **kwargs)
        print("<<耗时 %f %s" % (time() - start, "s"))
        return result
    return inner
