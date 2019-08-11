'''
双指针法
空间复杂度O(1)，时间复杂度O(n)
'''


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        l_str = list(s)
        head = 0
        tail = len(s) - 1
        while head < tail:
            if l_str[head] in vowels and l_str[tail] not in vowels:
                tail -= 1
            elif l_str[head] not in vowels and l_str[tail] in vowels:
                head += 1
            elif l_str[head] in vowels and l_str[tail] in vowels:
                l_str[head], l_str[tail] = l_str[tail], l_str[head]
                head += 1
                tail -= 1
            else:
                head += 1
                tail -= 1
        return ''.join(l_str)