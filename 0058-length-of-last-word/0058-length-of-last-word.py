class Solution:
    def lengthOfLastWord(self, s):
        i = len(s) - 1

        # Ignore spaces at the end
        while i >= 0 and s[i] == ' ':
            i -= 1

        count = 0

        # Count the last word
        while i >= 0 and s[i] != ' ':
            count += 1
            i -= 1

        return count