'''
如果石头的数量为4的倍数，那么就会输掉比赛
空间复杂度O(1)，时间复杂度O(1)
'''


class Solution:
    def canWinNim(self, n: int) -> bool:
        if n % 4 == 0:
            return False
        return True
