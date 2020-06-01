class Solution:
    def firstUniqChar(self, s: str) -> int:
        mm = dict()
        for ch in s:
            mm[ch] = mm.get(ch, 0)
        x = 0
        for i in s:
            if mm[i] == 1:
                return x
            x += 1
        return -1