class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            left=0
            right=len(word)-1
            palindrome=True
            while left<right:
                if word[left]!=word[right]:
                    palindrome=False
                    break 
                left+=1
                right-=1
            if palindrome:
                return word 
        return ""  