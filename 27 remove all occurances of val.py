class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        tnum = []
        for i in nums:
            if i != val:
                tnum.append(i)
        nums[:] = tnum
        return len(nums)
#has 23ms

#two pointer
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        n = len(nums)
        l = 0
        for r in range(n):
            if nums[r] != val:
                nums[l] = nums[r]
                l +=1
        return l

#in java 0ms
class Solution {
    public int removeElement(int[] nums, int val) {
        int t = 0;
        int n = nums.length;
        for (int i = 0; i< n; i++){
            if(nums[i]!=val){
                nums[t++] = nums[i]; //increment t after solving
            }
        }
        return t;        
    }
}
