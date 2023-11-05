class Solution:
    def isNonAlphaNumeric(self, c: chr) -> bool:
        if '0' <= c and c <= '9':
            return True # c is a digit
        if ('a' <= c and c <= 'z') or ('A' <= c and c <= 'Z'):
            return True # c is a letter
        return False

    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if not self.isNonAlphaNumeric(s[left]):
                left += 1
            elif not self.isNonAlphaNumeric(s[right]):
                right -= 1
            elif s[left].lower() != s[right].lower():
                return False
            else:
                left += 1
                right -= 1
        return True
