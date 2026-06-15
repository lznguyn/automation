class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = float('-inf')
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > max:
                max = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max
    
    def max(self, nums):
        nums = float('-inf')
        curr = 0
        for num in nums:
            curr += num
            if curr > max:
                max = curr
            if curr < 0:
                curr = 0
        return max