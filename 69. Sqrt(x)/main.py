class Solution:
    def mySqrt(self, x: int) -> int:
        i,j=1,x

        while(i<=j):
            mid=i+(j-i)//2
            if(mid*mid==x):
                return mid
            elif(mid*mid<x):
                i=mid+1
            elif(mid*mid>x):
                j=mid-1
        return j
        
