class Solution:
    def findRepeatedDnaSequences(self, s: str) -> list[str]:
        hashTable = {}
        if s == "":
            return 0
        else:
            start = 0
            while start+10 <= len(s):
                if not s[start:start+10] in hashTable:
                    hashTable[s[start:start+10]] = 1
                else:
                    hashTable[s[start:start+10]] += 1
                start += 1
        return list({k: v for (k, v) in hashTable.items() if (v >= 2)})


print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
