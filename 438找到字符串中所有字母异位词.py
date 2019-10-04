class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        window = {}
        needs = {}
        for c in p:
            needs[c] = needs.get(c, 0) + 1

        length, limit = len(p), len(s)
        left = right = 0

        while right < limit:
            c = s[right]
            # 当遇到不需要的字符时，将之前统计的信息全部放弃，从下一位置开始重新统计
            if c not in needs:
                window.clear()
                left = right = right + 1
            else:
                window[c] = window.get(c, 0) + 1  # 统计窗口内各种字符出现的次数
                if right - left + 1 == length:  # 当窗口大小与目标字符串长度一致时
                    if window == needs:
                        res.append(left)  # 如果窗口内的各字符数量与目标字符串一致就将left添加到结果中
                    window[s[left]] -= 1
                    left += 1
                right += 1
        return res
