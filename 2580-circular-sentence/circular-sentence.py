class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        ans=sentence.split(" ")
        for i in range(len(ans)):
            if ans[i][0]!=ans[i-1][-1]:
                return False
        return True        