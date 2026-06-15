class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        self.backtrack(nums, [], result)
        return result
    def backtrack(self, nums, path, result):
        if not nums:
            result.append(path)
            return
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            self.backtrack(nums[:i] + nums[i+1:], path + [nums[i]], result)
# nums = [1,1,2]
# i = 0, path = [], result = []
# backtrack([1,2], [1], result)
# i = 0, path = [1], result = []
# backtrack([2], [1,1], result)
# i = 0, path = [1,1], result = []
# backtrack([], [1,1,2], result)
# result = [[1,1,2]]
# i = 1, path = [1], result = [[1,1,2]]
# backtrack([1], [1,2], result)
# i = 0, path = [1,2], result = [[1,1,2]]
# backtrack([], [1,2,1], result)
# result = [[1,1,2], [1,2,1]]
# i = 1, path = [1], result = [[1,1,2], [1,2,1]]
# backtrack([1], [2,1], result) 
# i = 0, path = [2,1], result = [[1,1,2], [1,2,1]]
# backtrack([], [2,1,1], result)
# result = [[1,1,2], [1,2,1], [2,1,1]]
