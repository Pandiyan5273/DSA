
class Solution:
    def encode(self, s : str) -> str:
        if not s:
            return ""
    
        encoded_str = []
        count = 1
    
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:  # If current character matches previous
                count += 1
            else:
                encoded_str.append(s[i - 1] + str(count))  # Store previous character and count
                count = 1  # Reset count
    
        # Append last character and its count
        encoded_str.append(s[-1] + str(count))
    
        return "".join(encoded_str)



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        s = (input())
        
        obj = Solution()
        res = obj.encode(s)
        
        print(res)
        

        print("~")
# } Driver Code Ends