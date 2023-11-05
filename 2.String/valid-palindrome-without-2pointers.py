class Solution:
    def isNonAlphaNumberic(self, c: chr) -> bool:
        if '0' <= c and c <= '9':
            return True # c is a digit
        if 'a' <= c and c <= 'z':
            return True # c is a letter 
        return False

    def isPalindrome(self, s: str) -> bool:
        # "A man, a plan, a canal: Panama"
        new_str = ""
        for c in s.lower():
            if self.isNonAlphaNumberic(c):
                new_str += c
        
        n = len(new_str)
        for ind in range(n // 2):
            if new_str[ind] != new_str[n - ind - 1]:
                return False

        return True
