class Solution:
    def mySqrt(self, x: int) -> int:
        c=0
        temp=x
        if x==1:
            return 1
        for i in range(1,x,2):
            temp-=i  
            
            if temp<0:
                break
            c+=1
          
        return c
            