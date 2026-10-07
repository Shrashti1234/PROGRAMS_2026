class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sumd=0
        sumnd=0
        for i in range(1,n+1):
            if i%m==0:
                sumd+=i
            else:
                sumnd+=i
        return sumnd-sumd
        