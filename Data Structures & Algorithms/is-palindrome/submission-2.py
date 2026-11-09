class Solution:
    def isPalindrome(self, s: str) -> bool:
        aln = "".join([c.lower() for c in s if c.isalnum()])
        i = 0
        j = len(aln) - 1
        while i < j:
            if aln[i] == aln[j]:
                i += 1
                j -= 1
            else:
                return False

        return True