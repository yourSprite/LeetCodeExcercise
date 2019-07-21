'''
双指针
空间复杂度O(1)，时间复杂度O(N)
'''


class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        mid = len(s) // 2
        head = 0
        while head < mid:
            if s[head] != s[-head - 1]:
                return False
            head += 1
        return True
