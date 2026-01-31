class Solution(object):
    def lengthOfLongestSubstring(self, s):
        leftWindow = 0
        substring = set()
        max_length = 0

        for rightWindow in range(len(s)):
            while s[rightWindow] in substring:   
                substring.remove(s[leftWindow])
                leftWindow += 1
                
            substring.add(rightWindow)
            pass