from collections import Counter
class Solution:
    def sameFreq(self, s):
        freq=Counter(s)
        freqcount=Counter(freq.values())
        
        if len(freqcount)==1:
            return True
        if len(freqcount)>2:
            return False
        freqvalues=list(freqcount.keys())
        if 1 in freqvalues and freqcount[1]==1:
            return True
        h,l=max(freqvalues),min(freqvalues)
        if h==l+1 and freqcount[h]==1:
            return True
        return False    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        s = input()
        ob = Solution()
        answer = ob.sameFreq(s)
        if answer:
            print("true")
        else:
            print("false")

# } Driver Code Ends