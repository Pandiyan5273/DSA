//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    int countWays(string &s) {
        int n=s.size();
        if(n==0){
            return 0;
        }
        vector<int>dp(n+1,0);
        dp[0]=1;
        dp[1]=(s[0]=='0')?0:1;
        for(int i=2;i<=n;i++){
            int one=stoi(s.substr(i-1,1));
            int two=stoi(s.substr(i-2,2));
            if(one>=1 && one<=9){
                dp[i]+=dp[i-1];
            }
            if(two>=10 && two <=26){
                dp[i]+=dp[i-2];
            }
        }
        return dp[n];
    }
};


//{ Driver Code Starts.
int main() {
    int tc;
    cin >> tc;
    cin.ignore();
    while (tc--) {
        string digits;
        getline(cin, digits);
        Solution obj;
        int ans = obj.countWays(digits);
        cout << ans << "\n";

        cout << "~"
             << "\n";
    }
    return 0;
}
// } Driver Code Ends