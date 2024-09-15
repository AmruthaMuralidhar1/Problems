class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        i = mx = 0
        j = n-1
        while(i<j):
            temp = (j-i)*min(height[i],height[j])
            mx = max(mx, temp)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return mx
two pointer - take minimum of height becoause it can be that of the shorter side 
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        mxr = 0
        lp = 0
        rp = n-1
        while lp < rp:
            h = min(height[lp], height[rp])
            w = rp - lp
            temp = h * w
            mxr = max(mxr, temp)
            if height[lp] < height[rp]:
                lp += 1
            else:
                rp -= 1
        return mxr
accepted, two pointer

def garea(a, b):
        return a*b
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        mxr = 0
        for i in range(n):
            for j in range(i, n):
                a = min(height[i], height[j])
                h = abs(i-j)
                temp = garea(h, a)
                if(temp>mxr):
                    mxr = temp
        return mxr
time exceeded

