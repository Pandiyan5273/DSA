//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

// User function template for C++
class Solution {
  public:

    string printString(string s, char ch, int count) {
    int occurrence = 0;
    int index = -1;

    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ch) {
            occurrence++;
            if (occurrence == count) {
                index = i;
                break;
            }
        }
    }

    if (index == -1 || index == s.length() - 1) {
        return ""; 
    }

    return s.substr(index + 1);
    }
};


//{ Driver Code Starts.

int main() {

    ios_base::sync_with_stdio(0);
    cin.tie(NULL);
    cout.tie(NULL);

    int t;
    cin >> t;
    while (t--) {
        string s;
        char ch;
        int count;

        cin >> s >> ch >> count;
        Solution ob;
        cout << ob.printString(s, ch, count) << "\n";

        cout << "~"
             << "\n";
    }

    return 0;
}
// } Driver Code Ends