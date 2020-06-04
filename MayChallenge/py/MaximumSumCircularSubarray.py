
class Solution:
	def kadane(self, a):
		n, ma, sum = len(a), 0, 0
		for ai in a:
			sum += ai
			ma = max(ma, sum)
			sum = max(sum, 0)
		return ma

	def maxSubarraySumCircular(self, a: List[int]) -> int:
		from math import inf
		negative, ma = True, -inf

		for ai in a:
			ma = max(ma, ai)
			if ai >= 0:
				negative = False
				break
		if negative:
			return ma
		ans1, sum, n = self.kadane(a), 0, len(a)
		for i, ai in enumerate(a):
			sum += ai
			a[i] = -ai
		ans2 = sum + self.kadane(a)
		return max(ans1, ans2)


# int maxSubarraySumCircular(vector<int>& a) {
	
#     bool negative = true;int ma = -INT_MAX;
#     for(int i = 0;i < a.size();i ++) {
#         ma = max(ma, a[i]);
#         if(a[i] >= 0) {
#             negative = false;
#             break;
#         }
#     }
#     if(negative)
#         return ma;
	
#     int ans1 = kadane(a);
#     int sum = 0, n = a.size();
#     for(int i = 0; i < n;i ++) {
#         sum += a[i];
#         a[i] = (-1) * a[i];
#     }
#     int ans2 = sum + kadane(a);
#     return max(ans1, ans2);
# }
