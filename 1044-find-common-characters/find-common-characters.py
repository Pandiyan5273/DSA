class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        res=list(words[0])
        for i in range(1,len(words)):
            temp=[]
            for j in words[i]:
                if j in res:
                    temp.append(j)
                    res.remove(j)
            res=temp 
        return res 