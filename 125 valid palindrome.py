s = ''.join(c for c in s if c.isalnum())
        s = s.lower()
        if s == s[::-1]:
            return True
        return False
# two pointer approach with time O(n) and space O(1)
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Create a cleaned string containing only alphabetic characters
        clean = ""
        for char in s:
            if char.isalnum():
                clean += char.lower()  # Convert to lowercase to handle case insensitivity
        
        # Check if the cleaned string is a palindrome
        i = 0
        j = len(clean) - 1
        while i <= j:
            if clean[i] != clean[j]:
                return False
            i += 1
            j -= 1
        
        return True 
