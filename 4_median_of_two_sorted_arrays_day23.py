class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst=nums1+nums2
        for i in range(1,len(lst)):
            key=lst[i]
            j=i-1
            while j>=0 and key<lst[j]:
                lst[j+1]=lst[j]
                j-=1
                lst[j+1]=key
        y=0
        if (len(lst)%2!=0):
            y+=len(lst)//2
            return lst[y]
        else:
            a=len(lst)//2
            y=lst[a]+lst[a-1]
            return y/2
