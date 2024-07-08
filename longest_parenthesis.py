        n = len(s)
        dp = [0] * n  # dp[i] will store the length of the longest valid parentheses substring ending at index i
        max_length = 0
        
        # Iterate through the string
        for i in range(1, n):
            if s[i] == ')':
                if s[i-1] == '(':  # Case: '()'
                    dp[i] = (dp[i-2] if i >= 2 else 0) + 2
                elif i - dp[i-1] > 0 and s[i - dp[i-1] - 1] == '(':  # Case: '...))'
                    dp[i] = dp[i-1] + (dp[i - dp[i-1] - 2] if i - dp[i-1] >= 2 else 0) + 2
                max_length = max(max_length, dp[i])
        
        return max_length



class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []  # Use a stack to keep track of indices of '('
        max_length = 0
        
        # Iterate through the string
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)  # Push index of '(' to stack
            else:  # s[i] == ')'
                if stack and s[stack[-1]] == '(':  # If stack is not empty and top of stack is '('
                    stack.pop()  # Pop the '(' index from stack
                    # Calculate current valid substring length
                    current_length = i - stack[-1] if stack else i + 1
                    max_length = max(max_length, current_length)
                else:
                    stack.append(i)  # Push index of ')' to stack to mark invalid substring start
        
        return max_length
