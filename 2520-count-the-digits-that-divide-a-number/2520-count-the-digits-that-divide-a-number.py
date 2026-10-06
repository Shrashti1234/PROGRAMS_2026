class Solution:
    def countDigits(self, num: int) -> int:
        n=num
        count=0
        while n>0:
            
            d=n%10
            if d!=0 and num%d==0:
                count+=1
            n//=10
        return count

        