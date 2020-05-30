class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        freq, ans, index = [0, 0], 0, {0:-1}
        for i, num in enumerate(nums):
            freq[num] += 1
            if freq[0]-freq[1] in index:
                ans = max(ans, i-index[freq[0]-freq[1]])
            else:
                index[freq[0]-freq[1]] = i

        return ans

