class Solution(object):
    def findPermutationDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        dif = 0
        n = len(s)
        for i in range(n):
            for j in range(n):
                if s[i] == t[j]:
                    dif += abs(j - i)
        return dif
Optimal would be dictornary 
