//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {

  public:
    int minDifference(vector<int>& arr) {
        int sum=0;
        for(auto num:arr){
            sum+=num;
        }
        int n=arr.size();
        vector<bool>dp(sum+1,false);
        dp[0]=true;
        
        for(int num:arr){
            for(int j=sum;j>=num;j--){
                dp[j]=dp[j] || dp[j-num];
            }
        }
        
        int mindiff=sum;
        for(int i=0;i<=sum/2;i++){
            if(dp[i]){
                mindiff=min(mindiff,abs((sum-i)-i));
            }
        }
        return mindiff;
    }
};



//{ Driver Code Starts.
int main() {
    string ts;
    getline(cin, ts);
    int t = stoi(ts);
    while (t--) {

        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;
        while (ss >> number) {
            arr.push_back(number);
        }

        Solution ob;
        int ans = ob.minDifference(arr);

        cout << ans << endl;
    }
    return 0;
}
// } Driver Code Ends