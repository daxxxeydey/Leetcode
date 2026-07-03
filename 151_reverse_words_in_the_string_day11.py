class Solution:
    def reverseWords(self, s: str) -> str:
        sp=s.split()
        strg=""
        for i in sp[::-1]:
            strg=strg+i+" "
        return strg.rstrip()