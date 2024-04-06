def min_swaps(nums):
    # Count the number of 1's in the array
    ones_count = sum(nums)
    n = len(nums)
    
    # If there are no 1's in the array, return 0
    if ones_count == 0:
        return 0
    
    max_ones = 0
    # Count the number of 1's in the first window of size ones_count
    for i in range(ones_count):
        if nums[i] == 1:
            max_ones += 1
    
    # Initialize the number of swaps needed in the first window
    swaps_needed = ones_count - max_ones
    
    # Move the window and find the minimum swaps needed
    for i in range(1, n):
        # Update the number of 1's in the window
        if nums[i - 1] == 1:
            max_ones -= 1
        if nums[(i + ones_count - 1) % n] == 1:
            max_ones += 1
        
        # Update the minimum swaps needed
        swaps_needed = min(swaps_needed, ones_count - max_ones)
    
    return swaps_needed

# Example usage:
nums = [1, 0, 1, 0, 1]
print(min_swaps(nums))  # Output: 1
