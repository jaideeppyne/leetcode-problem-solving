
class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        low, high, ans = 1, n, n;
        while low <= high: 
            
            mid = (low + high) // 2;
            if(isBadVersion(mid)):
                high = mid - 1;
                ans = min(ans, mid);
            else:
                low = mid + 1;
        return ans;