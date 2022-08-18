from timeit import Timer


class Solution(object):
    # def twoSum(self, number, target):
    #     Map<Integer, Integer> hash = new HashMap<>();
    #     for (int i = 0; i < numbers.length; i++) {
    #         Integer diff = (Integer) (target - numbers[i]);
    #         if (hash.containsKey(diff)) {
    #             int toReturn[] = { hash.get(diff), i };
    #             return toReturn;
    #         }
    #         hash.put(numbers[i], i);
    #     }
    #     return new int[] {};
    def secondTwoSum(self, nums, target, /):
        source = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in source:
                return [source[diff], i]
            source[num] = i

    def threeTwoSum(self, nums, target, /):
        for i in range(len(nums)):
            a = target - nums[i]
            if a in nums and nums.index(a) != i:
                return i, nums.index(a)

    def twoSum(self, nums: list, target: int = 6, /) -> list:
        '''this is stupid algorithm'''
        # two point
        source = [(value, index) for index, value in enumerate(nums)]
        source.sort(key=lambda e: e[0])
        # print(nums_index)
        begin, end = 0, len(nums) - 1
        while begin < end:
            now = source[begin][0] + source[end][0]
            if now == target:
                return [source[begin][1], source[end][1]]
            elif now < target:
                begin += 1
            else:
                end -= 1


if __name__ == '__main__':
    # begin
    s = Solution()
    print(s.twoSum([3, 2, 4], 6))
    # description
    print(__name__)
    print(s.twoSum.__doc__)
    print(s.twoSum.__annotations__)

    print("-------------")
    print(Solution().secondTwoSum([3, 2, 4], 6))

    t1 = Timer("Solution().twoSum([3, 2, 4], 6)",
               "from __main__ import Solution")
    print("one ", t1.timeit(number=10000), "milliseconds")

    t2 = Timer(
        "Solution().secondTwoSum([3, 2, 4], 6)", "from __main__ import Solution")
    print("two ", t2.timeit(number=10000), "milliseconds")
    t3 = Timer(
        "Solution().threeTwoSum([3, 2, 4], 6)", "from __main__ import Solution")
    print("thr ", t3.timeit(number=10000), "milliseconds")
else:
    print("in model")
