class Solution(object):
    def lengthOfLastWord(self, s):
        sub_s = s.split()
        return len(sub_s[-1])

        