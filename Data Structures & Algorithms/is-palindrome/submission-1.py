class Solution:
    def isPalindrome(self, s: str) -> bool:
        aln = "".join([c.lower() for c in s if c.isalnum()])
        return aln == aln[::-1]