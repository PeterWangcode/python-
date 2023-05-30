class Solution:
    def patternRepeatedSubstring(self, s: str):
        n = len(s)
        index = 0
    
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                for j in range(i, n, i):
                    if s[0:i] == s[j:j + i]:
                        index = i
                    else:
                        index = 0
                        break
    
            if index >= 1:
                break
    
        return s[0:index] if index != 0 else s