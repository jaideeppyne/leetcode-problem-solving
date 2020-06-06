class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    
        ransom, mag = dict(), dict()
        for i in ransomNote:
            ransom[i] = ransom.get(i, 0) + 1
        for i in magazine:
            mag[i] = mag.get(i, 0) + 1
            
        for key, val in ransom.items():
            if val > mag.get(key, 0):
                return False
        return True