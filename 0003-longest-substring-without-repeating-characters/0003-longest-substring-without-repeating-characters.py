class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        l = 0
        length = 0

        for r in range(len(s)):
            if s[r] in freq and freq[s[r]] >= l:
                l = freq[s[r]] + 1
            freq[s[r]] = r
            length = max(length, r - l + 1)

        return length