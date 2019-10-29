'''
以每个点为中心，遍历各点计算距离并使用hashmap保存中间结果
空间复杂度O(n)，时间复杂度O(n**2)
'''


class Solution:
    def dist(self, point1, point2):
        return (point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        res = 0
        for i in points:
            hashMap = {}
            for j in points:
                d = self.dist(i, j)
                if i == j:
                    continue
                elif hashMap.get(d) is not None:
                    # 因为考虑到回旋镖位置可以调换，因此之前的结果要乘以2
                    res += hashMap[d] * 2
                    hashMap[d] += 1
                else:
                    hashMap[d] = 1
        return res
