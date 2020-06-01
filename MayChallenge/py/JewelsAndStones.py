
from sortedcontainers import SortedDict

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
    
        cnt = SortedDict()
        for stone in S:
            if stone in cnt:
                cnt[stone] += 1
            else:
                cnt[stone] = 1
        
        ans = 0
        for jewel in J:
            if jewel in cnt:
                ans += cnt[jewel]
        return ans
        