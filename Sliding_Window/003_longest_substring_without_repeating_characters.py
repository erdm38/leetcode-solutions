class Solution(object):
    def lengthOfLongestSubstring(self, s):
        leftWindow = 0
        substring = set()
        max_length = 0

        for rightWindow in range(len(s)):
            while s[rightWindow] in substring:   
                substring.remove(s[leftWindow])
                leftWindow += 1
                
            substring.add(s[rightWindow])
            
            max_length = max(max_length, rightWindow - leftWindow + 1)

        return max_length
    

# Time Complexity : O(N), where N is the length of the string s. Each character is processed at most twice (once added and once removed).
# Space Complexity : O(min(M, N)), where M is the size of the character set and N is the length of the string s. In the worst case, the sliding window will contain all unique characters from the string.
# The space complexity is determined by the size of the set used to store the characters in the current window.

# Zaman karmaşıklığı : O(N), burada N, s stringinin uzunluğudur. Her karakter en fazla iki kez işlenir (bir kez eklenir ve bir kez kaldırılır).
# Alan karmaşıklığı : O(min(M, N)), burada M karakter setinin boyutu ve N s stringinin uzunluğudur. En kötü durumda, kayan pencere stringden tüm benzersiz karakterleri içerecektir.
# Alan karmaşıklığı, mevcut penceredeki karakterleri depolamak için kullanılan setin boyutuna bağlıdır.