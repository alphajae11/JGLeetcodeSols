class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1="".join(c for c in s if c.isalnum())
        s1= s1.lower()
        for i in range(len(s1)):
            j = len(s1)-i-1
            if s1[i] != s1[j]:
                return False
        return True