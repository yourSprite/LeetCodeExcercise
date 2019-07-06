'''
方法一：双指针法，因此可以用快慢指针的方法，一个指向当前指针，一个遍历找到第一个不等于当前指针所指的数值的元素，
然后放到当前指针的后一位
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        p, q = 0, 1
        while q < len(nums):
            if nums[p] != nums[q]:
                nums[p + 1] = nums[q]
                p += 1
                q += 1
            else:
                q += 1
        return p + 1


'''
方法二：用字典判断列表是否重复，并把重复元素存在一个列表中，最后根据这个列表删除元素
额外空间超出O(1)，不合题意
'''


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        del_list = []
        dic = {}
        for i, num in enumerate(nums):
            if dic.get(num) is not None:
                del_list.append(num)
            else:
                dic[num] = 1

        for i, num in enumerate(del_list):
            nums.remove(num)

        print(nums)

        return len(nums)
