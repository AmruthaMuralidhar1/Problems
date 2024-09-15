        n = len(numbers)
        i = 0
        j = n - 1
        
        while i < j:
            current_sum = numbers[i] + numbers[j]
            if current_sum == target:
                return [i + 1, j + 1]  # Return indices in 1-based format
            elif current_sum < target:
                i += 1
            else:
                j -= 1
        
        return []  # Return an empty list if no solution is found
# two pointer, time complexity is O(n)
