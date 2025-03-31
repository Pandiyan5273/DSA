//{ Driver Code Starts
// Initial template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function template for C++

class Solution {
  public:
    int romanToDecimal(string &s) {
        unordered_map<char, int> romanValues = {  
        {'I', 1},  
        {'V', 5},  
        {'X', 10},  
        {'L', 50},  
        {'C', 100},  
        {'D', 500},  
        {'M', 1000}  
    };  

    int result = 0;  
    int n = s.length();  

    for (int i = 0; i < n; ++i) {  
        if (i < n - 1 && romanValues[s[i]] < romanValues[s[i + 1]]) {  
            result -= romanValues[s[i]];  
        } else {  
            result += romanValues[s[i]];  
        }  
    }  

    return result;  
    }
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        string s;
        cin >> s;
        Solution ob;
        cout << ob.romanToDecimal(s) << endl;

        cout << "~"
             << "\n";
    }
}
// } Driver Code Ends