class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
       l=[]
       for a in sentences:
        l.append(len(a.split()))
       return max(l)