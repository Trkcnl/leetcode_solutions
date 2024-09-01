class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0 if len(s) == 0 else 1
        curr_length = 0
        hashmap = {}

        for i in range(len(s)):
            hashmap[s[i]] = 1
            curr_length += 1

            for j in range(i+1, len(s)):
                if s[j] not in hashmap:
                    hashmap[s[j]] = 1
                    curr_length += 1
                else:
                    break

            hashmap = {}
            max_length = curr_length if (curr_length > max_length) else max_length
            curr_length = 0
        
        return max_length