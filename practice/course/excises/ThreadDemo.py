from threading import Thread
import time

class MyThread(Thread):
    def __init__(self, n):
        super(MyThread, self).__init__()
        self.n = n
        
    def run(self):
        print("task", self.n)
        time.sleep(1)
        print('2s')
        time.sleep(1)
        print('1s')
        time.sleep(1)
        print('0s')
        time.sleep(1)

def run(n):
    print("task", n)
    time.sleep(1)
    print('2s')
    time.sleep(1)
    print('1s')
    time.sleep(1)
    print('0s')
    time.sleep(1)

def demo1():
    t1 = Thread(target=run, args=("t1",))
    t2 = Thread(target=run, args=("t2",))
    t1.start()
    t2.start()
    
def demo2():
    t1 = MyThread("t1")
    t2 = MyThread("t2")
    t1.start()
    t2.start()
    
if __name__ == "__main__":
    demo2()