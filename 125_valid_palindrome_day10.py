class Solution:
    def isPalindrome(self, s: str) -> bool:
        emp=""
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                emp+=s[i].lower()
        return emp==emp[::-1]