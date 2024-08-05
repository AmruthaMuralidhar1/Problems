dp solution, bottom up, easy to understand, time o(n^2), space o(n)
def lis(self, nums):
  n = len(nums)
  dp = [1]*n
  for i in range(1, n):
    for j in range(i):
      if nums[i]>nums[j]:
        dp[i] = max(dp[i], dp[j]+1)
  return max(dp)



one line answers 
Code #1 - The Most Concise
Time complexity: technically it is O(n 
2
 ) because of list concatenation, but it runs as fast as O(n∗log(n)) solutions. Space complexity: O(n).

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return len(reduce(lambda l,q:l[:(i:=bisect_left(l,q))]+[q]+l[i+1:],nums,[]))
Code #2 - My Favorite, Quite Short, Walrus Free
Time complexity: O(n∗log(n)). Space complexity: O(n).

from sortedcontainers import SortedDict

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return (lambda d:any(setitem(d,bisect_left(d.values(),q),q) for q in nums) or len(d))(SortedDict())
Code #3 - Simple and Straightforward
Time complexity: O(n∗log(n)). Space complexity: O(n).

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return (l:=[]) or any(l.append(q) if(i:=bisect_left(l,q))==len(l) else setitem(l,i,q) for q in nums) or len(l)
Code #4 - Optimal Complexity, from namanr17
Time complexity: O(n∗log(n)). Space complexity: O(1).

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return (i:=0) or any(setitem(nums,(i:=i+1)-1 if(j:=bisect_left(nums,q,0,i))==i else j,
