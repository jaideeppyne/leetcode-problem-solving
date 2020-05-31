class Solution:
    def countBits(self, num: int) -> List[int]:
        builtin_popcount = lambda x: bin(x).count('1')
        return [builtin_popcount(i) for i in range(num+1)]

""" 
public:
    vector<int> countBits(int num) {
        
        vector<int> ans;
        for (int i = 0; i <= num; i++)
            ans.emplace_back(__builtin_popcount(i));
        return ans;
    }
}

 """