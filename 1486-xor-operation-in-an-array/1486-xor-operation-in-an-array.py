class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        i=0
        ans=0
        for i in range(0,n):
            ans=ans^(start+(2*i))
            i+=1
        return ans
        