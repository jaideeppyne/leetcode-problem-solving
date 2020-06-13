class RandomizedSet:
    from random import randint
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ss = set()
        self.a = []
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.ss:
            self.ss.add(val)
            self.a.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.ss:
            return False
        
        self.ss.discard(val)
        for i, ai in enumerate(self.a):
            if ai == val:
                self.a[i] = self.a[-1]
                self.a.pop()
                break
        return True
            
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.a[randint(0, len(a))]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()