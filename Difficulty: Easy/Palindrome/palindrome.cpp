//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function Template for C++

class Solution {
  public:
    bool isPalindrome(int n) {
    string s = to_string(n);  
    int l = 0, r = s.size() - 1;

    while (l < r) {
        if (s[l] != s[r])  
            return false;  
        l++;
        r--;
    }
    return true; 
    }
};


//{ Driver Code Starts.

int main() {
    int T;
    cin >> T;
    while (T--) {
        int n;
        cin >> n;
        Solution ob;
        bool ans = ob.isPalindrome(n);
        cout << (ans ? "true" : "false") << "\n~\n";
    }
    return 0;
}

// } Driver Code Ends