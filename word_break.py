def wordBreak(self, s, words):
    ok = [True]  # Initialize a list to store boolean values indicating if a substring can be broken into words
    for i in range(1, len(s)+1):
        ok += any(ok[j] and s[j:i] in words for j in range(i)),
    return ok[-1]


DFS method
class Solution(object):
    def wordBreak(self, s, wordDict):
        visited = set()  # To store visited substrings
        
        def dfs(start):
            if start == len(s):
                return True
            
            if start in visited:
                return False
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict and dfs(end):
                    return True
            
            visited.add(start)
            return False
        
        return dfs(0)
        
Recursion Method
class Solution(object):
    def wordBreak(self, s, wordDict):
        memo = {}

        def can_break(s):
            if s in memo:
                return memo[s]
            if not s:
                return True
            for i in range(1, len(s) + 1):
                if s[:i] in wordDict and can_break(s[i:]):
                    memo[s] = True
                    return True
            memo[s] = False
            return False

        return can_break(s)
