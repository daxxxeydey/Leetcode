class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tot=0
        lst=[]
        for i in nums:
            tot+=i
            lst.append(tot)
        return lst