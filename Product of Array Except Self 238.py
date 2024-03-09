test = [1, 2, 3, 4]
p = 1
ans = []
for i in test:
    p *= i
    
for i in range(0, len(test)):
    ans.append(int(p/test[i]))
    
print(ans)
#time complexity is O(n) 


def productExceptSelf(nums):
    n = len(nums)
    prefix_product = [1] * n
    suffix_product = [1] * n
    result = [1] * n

    # Calculate prefix products
    for i in range(1, n):
        prefix_product[i] = prefix_product[i - 1] * nums[i - 1]

    # Calculate suffix products
    for i in range(n - 2, -1, -1):
        suffix_product[i] = suffix_product[i + 1] * nums[i + 1]

    # Multiply prefix and suffix products to get result
    for i in range(n):
        result[i] = prefix_product[i] * suffix_product[i]

    return result

# Example usage:
nums = [1, 2, 3, 4]
print(productExceptSelf(nums))  # Output: [24, 12, 8, 6]

