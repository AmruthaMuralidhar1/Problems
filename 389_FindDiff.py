class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        rt = list(t)
        for i in s:
            if i in rt:
                rt.remove(i)
        return ''.join(rt)

