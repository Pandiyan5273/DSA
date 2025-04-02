# method prints the given pattern in a single line 
def printPattern(s):
    n = len(s)  
    mid = n // 2  
    ls=s[mid:]+s[:mid]
    for i in range(1,n+1):
        print(ls[:i],"$",sep="",end=" ")
    print()    


#{ 
 # Driver Code Starts
# Your Code goes here

if __name__=='__main__':
    n = int(input())
    for i in range(n):
        str = input().strip()
        printPattern(str)
        print("~")
# contributed by: Harshit Sidhwa
# } Driver Code Ends