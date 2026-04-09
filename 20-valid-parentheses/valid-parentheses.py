class Solution:
    def isValid(self, si: str) -> bool:
        s=[]
        for c in si:
            if c in "({[":
                s.append(c)
            elif c in ")}]":
                if not s:
                    return False
                t=s.pop()
                if t=="(" and c!=')' or t=="{" and c!='}' or t=='[' and c!=']':
                    return False
        return len(s)==0