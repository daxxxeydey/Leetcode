class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        return self.merge(nums)
    def merge(self,nums):
        if len(nums)>1:
            mid=len(nums)//2
            le=nums[:mid]
            r=nums[mid:]
            self.merge(le)
            self.merge(r)
            i=j=k=0
            while(i<len(le) and j<len(r)):
                if le[i]<r[j]:
                    nums[k]=le[i]
                    i+=1
                else:
                    nums[k]=r[j]
                    j+=1
                k+=1
            while(i<len(le)):
                nums[k]=le[i]
                i+=1
                k+=1
            while(j<len(r)):
                nums[k]=r[j]
                j+=1
                k+=1
        return nums
        