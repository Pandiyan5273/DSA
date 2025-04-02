//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends

class Solution {
  public:
    /*You are required to complete this method*/
    bool wildCard(string &txt, string &pat) {
    int n = txt.size(), m = pat.size();
    int i = 0, j = 0, starIdx = -1, match = 0;
    
    while (i < n) {
        if (j < m && (pat[j] == txt[i] || pat[j] == '?')) {
            i++, j++;
        } else if (j < m && pat[j] == '*') {
            starIdx = j++;
            match = i;
        } else if (starIdx != -1) {
            j = starIdx + 1;
            i = ++match;
        } else {
            return false;
        }
    }

    while (j < m && pat[j] == '*') j++;

    return j == m;
    }
};


//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        string pat, text;
        cin >> pat;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cin >> text;
        Solution obj;
        bool ans = obj.wildCard(text, pat);
        if (ans)
            cout << "true" << endl;
        else
            cout << "false" << endl;

        cout << "~"
             << "\n";
    }
}

// } Driver Code Ends