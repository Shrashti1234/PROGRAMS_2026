class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maxcount=0
        for sentence in sentences:
            count=len(sentence.split(" "))
            maxcount=max(maxcount,count)
        return maxcount