class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        count = 0
        counts, countt = {},{}

        if  n != len(t):
            return False

        for i in range(n):
            counts[s[i]] = 1 + counts.get(s[i], 0)
            countt[t[i]] = 1 + countt.get(t[i], 0)
            
        for c in counts:
            if counts[c] != countt.get(c, 0):
                return False
        
        return True