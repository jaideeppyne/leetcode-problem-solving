class Solution:
    def __init__(self):
        self.adj, self.visited, self.present_in_current_dfs = [[]], [], []
    def isCyclePresent(self, node, parent):
        self.visited[node] = True
        self.present_in_current_dfs[node] = True

        for child in self.adj[node]:
            if not self.visited[child] and self.isCyclePresent(child, node):
                return True
            elif self.present_in_current_dfs[child]:
                return True
        self.present_in_current_dfs[node] = False
        return False

    def canFinish(self, numCourses, prerequisites):
        self.visited = [False for _ in range(numCourses+1)]
        self.present_in_current_dfs = [False for _ in range(numCourses+1)]
        self.adj = [[] for _ in range(numCourses+1)]
        for i in range(len(prerequisites)):
            self.adj[prerequisites[i][1]+1].append(prerequisites[i][0] + 1)
        
        ans = True
        for i in range(numCourses+1):
            if not self.visited[i] and self.isCyclePresent(i, 0):
                ans = False
        self.adj, self.visited = [], []
        self.present_in_current_dfs = []
        return ans


""" 
class Solution {
public:
    vector<vector<int>> adj;
    vector<bool> visited, present_in_current_dfs;
    
    //DFS for cycle detection in "directed" graph
    bool isCyclePresent(int node, int parent) {
        
        visited[node] = present_in_current_dfs[node] = true;
        
        for (int child : adj[node]) {
            if(!visited[child] and isCyclePresent(child, node))
                return true;
            else if(present_in_current_dfs[child])
                return true;
        }
        present_in_current_dfs[node] = false;
        return false;
    }
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        
        visited.assign(numCourses + 1, false);
        present_in_current_dfs.assign(numCourses + 1, false);
        adj.resize(numCourses + 1);
        
        for (int i = 0; i < prerequisites.size(); i++)
            adj[prerequisites[i][1] + 1].emplace_back(prerequisites[i][0] + 1);
        
        bool ans = true;
        for (int i = 1; i <= numCourses; i++)
            if (!visited[i] and isCyclePresent(i, 0))
                ans = false;
        
        adj.clear();
        visited.clear();
        present_in_current_dfs.clear();
        
        return ans;
    }
}; """