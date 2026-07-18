class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d=set()
        le=0
        ans=0
        for i in range(len(s)):
            while s[i] in d:
                d.remove(s[le])
                le+=1
            d.add(s[i])
            ans=max(ans,i-le+1)
        return ans