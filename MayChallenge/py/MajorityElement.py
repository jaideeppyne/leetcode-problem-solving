
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
    	n, majority_size = len(nums), len(nums)/2
    	mm = dict()
    	for i in nums:
    		mm[i] = mm.get(i, 0) + 1
    		if mm[i] > majority_size:
    			return i
    	return -1

