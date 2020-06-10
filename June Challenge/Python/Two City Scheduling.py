class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda cost: cost[0]-cost[1])
        n, ans = len(costs), 0
        for i in range(n):
        	if 2*i < n:
        		ans += costs[i][0]
        	else:
        		ans += costs[i][1]
        return ans

