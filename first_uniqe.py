class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_count = {}
    
    # Count occurrences of each character
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        # Find the index of the first non-repeating character
        for i, char in enumerate(s):
            if char_count[char] == 1:
                return i
        
        # If no non-repeating character found, return -1
        return -1  
