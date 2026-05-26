class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        cnt=0
        v=set()
        for i in range(len(word)-1):
            for j in range(i+1,len(word)):
                if abs(ord(word[i])-ord(word[j]))==32:
                    ch=word[i].lower()
                    if ch not in v:
                        v.add(ch)
                        cnt+=1
        return cnt