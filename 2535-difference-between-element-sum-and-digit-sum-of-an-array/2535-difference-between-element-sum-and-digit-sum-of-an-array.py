class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        sum=0
        digitsum=0
        for num in nums:
            sum+=num
            while num>0:
                d=num%10
                digitsum+=d
                num//=10
        diff=sum-digitsum
        return diff

        