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
    def twoSum(self, nums:list, target:int = 6)->list:
        '''this is stupid algorithm'''
        # two point
        nums_index = [(v, index) for index, v in enumerate(nums)]
        print(nums_index)
        nums_index.sort()
        begin, end = 0, len(nums) - 1
        while begin < end:
            curr = nums_index[begin][0] + nums_index[end][0]
            if curr == target:
                return [nums_index[begin][1], nums_index[end][1]]
            elif curr < target:
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
else:
    print("hah")