class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        merged = []
        for current in intervals:
            if not merged or current[0] > merged[-1][1]:
                merged.append(current)
            else:
                merged[-1][1] = max(merged[-1][1], current[1])
        merged.append(newInterval)
        merged.sort(key=lambda x: x[0])
        result = [merged[0]]
        for current in merged[1:]:
            last = result[-1]
            if current[0] <= last[1]:
                result[-1] = [last[0], max(last[1], current[1])]
            else:
                result.append(current)
        return result