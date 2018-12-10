class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        使用双端队列，将最大值保存在队列头部，每次返回头部元素
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums: return []
        window, res = [], []# windows中保存元素下标，为双端队列,res用来保存结果
        for i, x in enumerate(nums):# 循环nums中所有元素
            if i >= k and window[0] < i-(k-1):
                window.pop(0)
            while window and nums[window[-1]] <= x:
                window.pop()
            window.append(i)# 向window中添加元素下标
            if i+1 >= k:# i的下标从0开始
                res.append(nums[window[0]])
        return res
