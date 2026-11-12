class Solution(object):
    def characterReplacement(self, s, k):
        count = {}
        left = 0
        max_count = 0
        result = 0

        for r in range(len(s)):
            char = s[r]

            count[char] = count.get(char, 0) + 1

            max_count = max(max_count, count[char])

            while (r - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
            result = max(result, r - left + 1)
            
        return result
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        