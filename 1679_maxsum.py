class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()  # Sort the array
        lp = 0
        rp = len(nums) - 1
        res = 0
        
        while lp < rp:
            curr_sum = nums[lp] + nums[rp]
            if curr_sum == k:
                res += 1
                lp += 1  # Move left pointer to the right
                rp -= 1  # Move right pointer to the left
            elif curr_sum < k:
                lp += 1  # If sum is less than k, move left pointer to the right
            else:
                rp -= 1  # If sum is greater than k, move right pointer to the left
        
        return res
in two pointer you first sort the array
