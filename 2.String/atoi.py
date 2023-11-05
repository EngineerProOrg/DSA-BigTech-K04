class Solution:
    MIN_INT = - 2 ** 31
    MAX_INT = 2 ** 31 - 1
    def outOfIntRange(self, n: int, neg_sign: bool) -> bool:
        n = n * (-1 if neg_sign else 1)
        return n < self.MIN_INT or n > self.MAX_INT

    def myAtoi(self, s: str) -> int:
        # remove leading whitespaces
        s = s.lstrip()
        # check the sign
        negative = False
        if len(s) > 0 and (s[0] in ['-', '+']):
            negative = s[0] == '-'
            s = s[1:]
        # construct number
        number = 0
        for c in s:
            if c.isdigit():
                number = number * 10 + (ord(c) - ord('0'))
                if self.outOfIntRange(number, negative):
                    break
            else:
                break
        number *= (-1 if negative else 1)
        number = max(number, self.MIN_INT)
        number = min(number, self.MAX_INT)
        return number
