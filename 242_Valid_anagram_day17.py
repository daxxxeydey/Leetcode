class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def countord(s):
            l=[]
            for i in s:
                l.append(ord(i))
            return l
        ct=countord(t)
        cs=countord(s)
        for i in countord(s):
            if i in ct:
                ct.remove(i)
                cs.remove(i)
        return ct==[] and cs==[]