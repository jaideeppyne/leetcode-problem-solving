class Solution:
    def countBits(self, num: int) -> List[int]:
        bitCount = lambda x: bin(x).count('1')

        return [bitCount(i) for i in range(num+1)]