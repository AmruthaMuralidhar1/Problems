class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0  # Handle edge case where nums is empty
        j = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1
        return j


with temporary array
class Solution:
    def removeDuplicates(self, nums):
        tnum = []
        tnum.append(nums[0])
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                tnum.append(nums[i])
        tnum.sort()
        nums[:] = tnum      
        return len(nums)

in java
import java.util.Arrays;

class Solution {
    public int removeDuplicates(int[] nums) {
        int j = 0;
        int n = nums.length;
        if (n == 0) return 0; // Handle edge case where nums is empty
        int[] temp = new int[n];
        temp[j++] = nums[0]; // Always include the first element
        for (int i = 1; i < n; i++) {
            if (nums[i] != nums[i - 1]) {
                temp[j++] = nums[i];
            }
        }
        // Now, temp contains unique elements but might have some trailing zeros
        // Copy temp back to nums, removing trailing zeros
        for (int k = 0; k < j; k++) {
            nums[k] = temp[k];
        }
        return j;
    }
}
