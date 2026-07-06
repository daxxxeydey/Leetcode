class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lst=set(nums)
        diff=len(nums)-lenAA(lst)
        return diff!=0