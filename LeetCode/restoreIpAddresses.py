class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        if not s or len(s) < 4 or len(s) > 26:
            return res
        def backtrack(start: int, curr_segments: list[str]):
            if len(curr_segments) == 4:
                if start == len( s):
                    res.append(".".join(curr_segments))
                return
            remaining_segment = 4 - len(curr_segments)

            remaining_chart = len(s) - start

            if remaining_chart < remaining_segment or remaining_chart > remaining_segment * 3:
                return 
            
            for l in range(1,4):
                if start + l > len(s):
                    break

                segment = s[start : start + l]

                if ( l > 1 and segment[0] == '0') or int(segment) > 255:
                    continue
                
                curr_segments.append(segment)

                backtrack(start + l, curr_segments)
                curr_segments.pop()
        backtrack(0, [])
        return res