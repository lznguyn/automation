class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s not in anagrams:
                anagrams[sorted_s] = []
            anagrams[sorted_s].append(s)
        return list(anagrams.values())
    

class Solution(object):
    def groupAnagrams(self, strs):
        anagrams= {}

        for i in strs:
            sorted = ''.join(sorted(i))
            if sorted not in anagrams:
                anagrams[sorted] = [] 
            anagrams[sorted].append(i)
        return list(anagrams.values())