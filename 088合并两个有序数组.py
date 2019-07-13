'''
方法一：由题意len(nums1) >= m + n，可直接在nums1中操作，使用双指针从后往前比较
空间复杂度O(1)，时间复杂度O(m+n)
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        p = m + n - 1
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        nums1[:p2 + 1] = nums2[:p2 + 1]

'''
方法二：使用双指针从前往后比较，并使用一个额外数组存储结果
空间复杂度O(m+n)，时间复杂度O(m+n)
'''
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        res = []
        p1 = 0
        p2 = 0
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        nums1[:] = res + nums1[p1:m] + nums2[p2:n]



'''
方法三：扩展到去掉len(nums1) >= m + n条件
空间复杂度O(1)，时间复杂度O(m+n)
'''


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n == 0:
            nums1[:] = []
        elif m == 0 and n != 0:
            nums1[:] = nums2[:n]
        elif m != 0 and n == 0:
            nums1[:] = nums1[:m]
        else:
            nums1[:] = nums1[:m]
            nums2[:] = nums2[:n]
            p1 = 0
            p2 = 0
            while p2 < n:
                if nums1[p1] >= nums2[p2]:
                    nums1.insert(p1, nums2[p2])
                    p1 += 1
                    p2 += 1
                elif p1 == len(nums1) - 1:
                    nums1.append(nums2[p2])
                    p2 += 1
                else:
                    p1 += 1
