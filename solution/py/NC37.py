# 合并区间
from functools import cmp_to_key
import itertools
from typing import List


class Interval:
    def __init__(self, a=0, b=0):
        self.start = a
        self.end = b

    def __str__(self) -> str:
        return f"[{self.start}, {self.end}]"


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        res = []
        # fast-fail
        if len(intervals) <= 0:
            return res
        intervals.sort(key=cmp_to_key(lambda x, y: x.start - y.start))
        res.append(intervals[0])
        for i in range(len(intervals)):
            if intervals[i].start <= res[-1].end:
                res[-1].end = max(res[-1].end, intervals[i].end)
            else:
                res.append(intervals[i])
        return res


if __name__ == '__main__':
    a_list = [1,2,"d", True]
    b_map = {}
    b_map["a"] = 1
    b_map[2] = "b"
    print(b_map)
    print(a_list)
    print(["".join(e) for e in itertools.permutations("aab")])
    print([e for e in set(itertools.permutations("aab"))])
    result = Solution().merge(list([Interval(10, 30), Interval(
        20, 60), Interval(80, 100), Interval(150, 180)]))
    for item in result:
        print(item, end=" ")
