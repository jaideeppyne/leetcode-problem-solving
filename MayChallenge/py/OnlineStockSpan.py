class StockSpanner:
	from math import inf
	def __init__(self):
		self.prices = [inf]
		self.dp = [0]

	def next(self, price: int) -> int:
		val = 1
		while len(self.prices) and price >= self.prices[-1]:
			self.prices.pop()
			val += self.dp[-1]
			self.dp.pop()

		self.dp.append(val)
		self.prices.append(price)
		return self.dp[-1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

