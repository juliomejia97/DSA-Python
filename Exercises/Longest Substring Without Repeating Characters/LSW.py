class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        else:
            start = 0
            end = 0
            max_len = 0
            unique_elements = set()
            while end < len(s):
                if s[end] not in unique_elements:
                    unique_elements.add(s[end])
                    end += 1
                    max_len = max(max_len, len(unique_elements))
                else:
                    unique_elements.remove(s[start])
                    start += 1
        return max_len


print(Solution().lengthOfLongestSubstring("pwwkew"))
