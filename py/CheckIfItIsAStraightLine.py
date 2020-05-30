class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        from math import gcd
        # check if slope of each pair of lines is same

        def getSlope(x, y):
            upper, lower = abs(x[1] - y[1]), abs(x[0] - y[0])
            common = gcd(upper, lower)
            return (upper//common, lower//common)
            
        
        slope = getSlope(coordinates[0], coordinates[1])
        
        for p1 in coordinates:
            for p2 in coordinates:
                if p1 != p2 and slope != getSlope(p1, p2):
                        return False
        return True
    