from big_o import big_o, datagen

# 估算排序函数 stored 的 大O 数量级

best, others = big_o(
    func=sorted,  # 计算的函数
    data_generator=lambda n: datagen.integers(n, 10000, 50000),  # 产生输入参数的函数
    min_n=1000,  # 最小N
    max_n=100000,  # 最大N
    n_measures=100  # 取多少个N
    # n_repeats # 重复执行多次计算函数func, 来统计执行时间
    # n_timings # 重复测量多少次 (保留最好的测量结果)
)

print(best)
# Linearithmic: time = 0.00039 + 9.4E-09*n*log(n) (sec)
#                      0.00039+9.4e-09 = 0.0003900094

# 通用的 data_generator
# big_o.datagen.n_(n) 就返回n
# big_o.datagen.integers(n) 返回n个随机整数list
# big_o.datagen.range_n(n) 返回参数n的列表list

# 返回 n 个随机数数组


def f(n): return datagen.integers(n, 10000, 50000)


print(f(2))

# OJ Online Judge IPO Input Process Output
# 输入什么 做什么 输出什么
# 看清样例
