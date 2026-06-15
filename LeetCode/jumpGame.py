class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0 
        current_end = 0
        farthest = 0
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
        return jumps
    

[2,3,1,1,4]

# i = 0, jumps = 0, current_end = 0, farthest = 0
# farthest = max(0, 0 + 2) = 2
# i == current_end => jumps = 1, current_end = 2
# i = 1, jumps = 1, current_end = 2, farthest = 2
# farthest = max(2, 1 + 3) = 4
# i = 2, jumps = 1, current_end = 2, farthest = 4
# i == current_end => jumps = 2, current_end = 4
# i = 3, jumps = 2, current_end = 4, farthest = 4
# i = 4, jumps = 2, current_end = 4, farthest = 4
# return 2