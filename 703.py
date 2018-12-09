class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k# 堆的元素个数
        self.heap = nums
        self.size = len(nums)
        heapq.heapify(self.heap)# 将数组转换为堆
        while self.k < self.size:# 调整堆大小至k
            heapq.heappop(self.heap)
            self.size -= 1
        

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        # 如果栈为空，将bal推入heap
        if len(self.heap) == 0:
            heapq.heappush(self.heap, val)
        # 如果栈长度小于k，将val推入heap
        elif self.k > len(self.heap):
            heapq.heappush(self.heap, val)
        # 如果val大于heap中最小值，val替换heap中最小值
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
