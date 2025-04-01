class Solution:
    def maximumProfit(self, prices):
        mini=float('inf')
        maxi=0
        for price in prices:
            mini=min(mini,price)
            p=price-mini
            maxi=max(maxi,p)
        return maxi    





#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        prices = list(map(int, input().split()))
        # Create a Solution object and calculate the result
        obj = Solution()
        result = obj.maximumProfit(prices)
        # Print the result
        print(result)

# } Driver Code Ends