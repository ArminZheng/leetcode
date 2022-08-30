import random
import time

from basic.LinearDS.simpleQueue import Queue
from basic.LinearDS.simpleDeque import Queue as DQueue

"""打印机问题
确定打印机系统的容量: 在能接受的等待时间内, 先到先服务, 容纳多少用户以多高频率提交多少打印任务

实例
    1. 1 hr, 10 students present
    2. 每人发起 2 次打印, 每次 1~20 页
    3. 打印机性能:
        a. draft: 10 paper/m
        b. normal: 5 paper/m

    - 实例目标: Print as much better quality as possible without waiting too long

对问题建模 (抛弃对问题没有实质关系的细节)
    1. 对象: 打印任务、打印队列、打印机
        - 打印任务: 提交时间、打印页数
        - 打印队列: 具有FIFO性质的打印任务队列
        - 打印机: 打印速度、是否忙

    2. 过程
        1. 确定生成概率
        2. 确定打印页数
        3. 实施打印
        4. 模拟时间
        
        例子:
            1. 20/60*60 = 1/180 start/s
            2. 1~20 paper probability equal
            3. current print work + print complete countdown
            4. unity time framework: one unit time must be start print and execute (1:1)
"""


class Task:
    def __init__(self, time) -> None:
        self.__timestamp = time
        self.__pages = random.randrange(1, 20 + 1)

    @property
    def pages(self):
        return self.__pages

    @property
    def stamp(self):
        return self.__timestamp

    def waitTime(self, current_time):
        return current_time - self.__timestamp


class Printer:

    def printTask():
        """打印任务
        决策支持问题, 但无法通过规则直接计算, 需要进行模拟打印任务场景, 
        然后对运行结果进行分析, 以支持对打印机模式设定的「决策」
        建模: 
            固定时间转化为速率, 在划分单位时间. 时间用尽, 统计平均等待时间
            重要的是中间, 时间按照秒为单位来流失, 每秒钟都要进行建模过程

        """
        pass

    def __init__(self, ppm) -> None:
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task != None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        if self.current_task != None:
            return True
        else:
            return False

    def startNext(self, new_task: Task):
        self.current_task = new_task
        self.time_remaining = new_task.pages * 60/self.page_rate


def newPrintTask():
    """ 1/180 概率生成作业 """
    num = random.randrange(1, 180 + 1)
    return True if num == 180 else False


def simulation(num_seconds, page_per_minute):  # 模拟
    lab_printer = Printer(page_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):  # 时间流逝
        if newPrintTask():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.isEmpty()):
            next_task: Task = print_queue.dequeue()
            waiting_times.append(next_task.waitTime(current_second))
            lab_printer.startNext(next_task)

        lab_printer.tick()

    average_wait: float = sum(waiting_times) / len(waiting_times)
    print("Average Wait %6.2f secs %3d task remaining" %
          (average_wait, print_queue.size()))
    return average_wait, print_queue.size()


if __name__ == '__main__':
    """
    为了对打印模式进行决策, 我们用模拟程序, 仿真, 来评估任务等待时间

    模拟系统对现实的仿真: 在不耗费现实资源(资源比较昂贵)的情况下, 可以通过不同的设定, 反复多次模拟来帮助我们进行决策
    """
    count, all = 0, 0
    for i in range(10):
        average, remaining = simulation(3600, 5)
        if remaining == 0:
            count += 1
            all += average
    print("total average:", all / count)
    """
    Average Wait  74.95 secs   1 task remaining
    Average Wait 121.18 secs   0 task remaining
    Average Wait  61.20 secs   0 task remaining
    Average Wait  59.57 secs   2 task remaining
    Average Wait 137.53 secs   0 task remaining
    Average Wait  33.30 secs   2 task remaining
    Average Wait   6.00 secs   0 task remaining
    Average Wait  82.33 secs   0 task remaining
    Average Wait 562.08 secs   2 task remaining
    Average Wait 133.67 secs   0 task remaining
    total average: 90.31713106295149
    """
    count, all = 0, 0
    for i in range(10):
        average, remaining = simulation(3600, 10)
        if remaining == 0:
            count += 1
            all += average
    print("total average:", all / count)
    """
    Average Wait  19.38 secs   0 task remaining
    Average Wait   7.44 secs   0 task remaining
    Average Wait  12.15 secs   0 task remaining
    Average Wait  22.36 secs   1 task remaining
    Average Wait  17.00 secs   0 task remaining
    Average Wait  22.52 secs   0 task remaining
    Average Wait  10.48 secs   0 task remaining
    Average Wait  29.91 secs   2 task remaining
    Average Wait  17.50 secs   0 task remaining
    Average Wait  15.42 secs   0 task remaining
    total average: 15.234782703285992
    """

"""
1. 使用旋转手臂的力量, 小拇指并不需要发力
2. 尽量少移动, 因为重新定位很耗时
3. 手臂应该悬停, 而不是放在桌子或者腕托上

- 热键:
        wert  io
    asd     h  l
            nm
- 易错词:
    assert
    hand
    everything
    few wert
    
    switch
    subtract
    extends
    synchronized
    append
    implements
    throwas
    volatile
    protect
    catch
    break
"""
