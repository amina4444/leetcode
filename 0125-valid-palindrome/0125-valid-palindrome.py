class Solution(object):
    def isPalindrome(self, s):
        c_s = ""
        for ch in s:
            if ch.isalnum():
                c_s += ch.lower()
        return c_s == c_s[::-1]
        """
        :type s: str
        :rtype: bool
        """
        