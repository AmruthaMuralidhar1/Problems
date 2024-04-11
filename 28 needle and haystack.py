#string slicing string_namr[start_index: stop_index: step]
#arr[start:stop]         # items start through stop-1
#arr[start:]             # items start through the rest of the array
#arr[:stop]              # items from the beginning through stop-1
#arr[:]                  # a copy of the whole array
#arr[start:stop:step]    # start through not past stop, by step
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        m = len(needle)
        n = len(haystack)
        for i in range(n):
            t = haystack[i: i+m: 1]
            if t == needle:
                return i
        return -1

#16 ms

#in java 0ms
class Solution {
    public int strStr(String haystack, String needle) {
        int m = needle.length();
        int n = haystack.length();
        String t;
        for(int i = 0; i<= n-m; i ++){
            t = haystack.substring(i, i+m);
            if(t.equals(needle)){
                return i;
            }
        }
        return -1;     
    }
}
