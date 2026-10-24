class Solution(object):
    def isValid(self, s):
        stack = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for i in range(len(s)):
            if s[i] in "({[":
                stack.append(s[i])
            elif s[i] in ")]}":
                if not stack or stack[-1] != pairs[s[i]]:
                    return False
                stack.pop()

        return len(stack) == 0
        
                

        """
        :type s: str
        :rtype: bool
        """
        