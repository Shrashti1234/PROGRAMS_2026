class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        letters=set()
        for ch in sentence:
            letters.add(ch)
        return len(letters)==26
            
        