class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s=0
        l=[0]
        for i in gain:
            s+=i
            l.append(s)
            
        return max(l)